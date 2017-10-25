#!/usr/bin/python3

import logging
import sqlite3

class NetworkDatabase(object):
    def __init__(self, filename="network.db"):
        self.dbfilename = filename
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute(
            "CREATE TABLE IF NOT EXISTS records\
            ( record_internal_id INTEGER PRIMARY KEY, \
            ip     TEXT, \
            mac TEXT , \
            time_last TEXT , \
            confiance TEXT , \
            status   TEXT \
            )" \
        )
        db.commit()
        c.close()

    def add_record(self, ip = '', mac = '', time_last = '' , confiance = '' , status = ''):
        logging.info("Ajout dans la BDD: %s, %s, %s, %s, %s" % (ip, mac, time_last, confiance, status))
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('INSERT INTO records(ip, mac, time_last, confiance, status) \
                    VALUES(?,?,?,?,?)', (ip, mac, time_last, confiance, status))
        db.commit()
        c.close()

    def update_record(self, record_id, ip = '', mac = '', time_last = '' , confiance = '' , status = ''):
        logging.info("Mise a jour dans la BDD: %s, %s, %s, %s, %s " % (ip, mac, time_last, confiance, status))
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('UPDATE records set ip=?, mac=?, time_last=?, confiance=?, status=? \
                    WHERE record_internal_id=?', (ip, mac, time_last, confiance, status, \
                                                        record_id))
        db.commit()
        c.close()

    def delete_record(self, record_id):
        logging.info("Suppression dans la BDD de l id: %s " % record_id)
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('DELETE FROM records where record_internal_id=?', (record_id,))
        db.commit()
        c.close()

    def list_all_records(self, ):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('SELECT * from records')
        records = c.fetchall()
        c.close()
        return records

    def get_record(self, record_id):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('SELECT * from records WHERE record_internal_id=?', (record_id,))
        records = c.fetchall()
        c.close()
        return records[0]

    def get_record_from_ip_mac(self, ip, mac):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('SELECT * from records WHERE ip=? AND mac=?', (ip,mac,))
        records = c.fetchall()
        c.close()
        logging.info(records)
        if len(records) != 0 :
            return records[0]
        else:
            return ""
