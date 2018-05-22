#!/usr/bin/env python2
import json
import thread

import psycopg2
import websocket

import api
import config


def on_message(ws, message):
    #print(message)
    j = json.loads(message)
    try:
        result_ = j["params"][1][0]
        result_.reverse()
        ops = set()
        for d in result_:
            id_ = d["id"]
            print(id_)
            if id_[:4] == "2.9.":
                op_id = d["operation_id"]
                if op_id in ops:
                    continue
                ops.add(op_id)

                #print j["params"][1][0][0]
                data = api._get_object(id_)
                #print data[0]
                account_id = data[0]["account"]
                data_a = api._account(account_id)

                #print data_a[0]["name"]
                account_name = data_a[0]["name"]

                data2 = api._get_object(data[0]['operation_id'])
                block_num = data2[0]["block_num"]

                op_type = data2[0]["op"][0]

                #print block_num
                trx_in_block =  data2[0]["trx_in_block"]
                op_in_trx =  data2[0]["op_in_trx"]

                con = psycopg2.connect(**config.POSTGRES)
                cur = con.cursor()
                query = "INSERT INTO ops (oh, ath, block_num, trx_in_block, op_in_trx, datetime, account_id, op_type, account_name) VALUES(%s, %s, %s, %s, %s, NOW(), %s, %s, %s)"
                print query
                cur.execute(query, (id_, data[0]['operation_id'], str(block_num), str(trx_in_block), str(op_in_trx), account_id, str(op_type), account_name))
                con.commit()
    except:
        pass


def on_error(ws, error):
    print(error)
    #print ""


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        ws.send('{"method": "set_subscribe_callback", "params": [5, true], "id": 6}')

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(config.WEBSOCKET_URL,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    ws.run_forever()
