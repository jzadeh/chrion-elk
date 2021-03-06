import pandas as pd
import logging, os
import ipaddress
#from pprint import pprint

log = logging.getLogger(__name__)

class p0f_ingestion:
"""Parse p0f related data

  Attributes:
  directory_to_parse: path to p0f data
  move_files_after_parsing: set to false if we want to retain files after parsing
  delog: to remove files in set directory
  inFile: to read data in log"""

    def __init__(self, directory_to_parse, move_files_after_parsing = true):
        self.directory = directory_to_parse
        self.flag = move_files_after_parsing

    def move_data(delog):
#excute an os command to read all files in directory and delete
        os.system('rm '+delog)

    def p0f_parse(inFile):
        df2 = pd.read_csv( inFile,sep='|',header=0, engine='python')
        df2.columns = ['time','client_ip','server_ip','d','connection','mtu','g','raw_ip']
        df2['client_ip'] = df2['client_ip'].map(lambda x: str(x)[4:])
        df2['server_ip'] = df2['server_ip'].map(lambda x: str(x)[4:])
        df2['mtu'] = df2['mtu'].map(lambda x:  x.lstrip('raw_mtu=langEnglishnonefreqdistHz').rstrip('=Hz'))
        df2['time'] = df2['time'].map(lambda x:  x.lstrip('').rstrip('mod=mtu,cli=mod=syn+ackmod=uptimemod=httpreqmod= httpmod=host chang'))
        df2_checkpub = df2['client_ip'].apply(lambda x: ipaddress.ip_address(x).is_global)
        df2_checkpriv = df2['client_ip'].apply(lambda x: ipaddress.ip_address(x).is_private)
        df2['cip'] = df2['client_ip'].apply(lambda x: x.split('/')[0])
        df2['sip'] = df2['server_ip'].apply(lambda x: x.split('/')[0])
        # df2_cipcheckpub = df2['cip'].apply(lambda x: ipaddress.ip_address(x).is_global)
        # df2_cipcheckpriv = df2['cip'].apply(lambda x: ipaddress.ip_address(x).is_private)
        # df2_sipcheckpub = df2['sip'].apply(lambda x: ipaddress.ip_address(x).is_global)
        # df2_sipcheckpriv = df2['sip'].apply(lambda x: ipaddress.ip_address(x).is_private)
        return (df2)
    #def logwrite():
        #df2 = df2.to_csv('p0f.csv', index=None, encoding='utf-8')
