#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# author wwqgtxx <wwqgtxx@gmail.com>


import urllib.request,io,os,sys,json,re,math,subprocess,traceback

try:
    from ..lyp_pv import run
except Exception as e:
    from lyp_pv import run

try:
    from .. import common
except Exception as e:
    import common
    


class LypPvParser(common.Parser):

    filters = run.GetVersion()['filter'] 

    # parse functions
    def Parse(self,url,types=None):
        if (types is not None) and ("formats" not in types):
            return
        print("call lyp_pv.run.Parse("+url+")")
        out = run.Parse(url)
        for data in out['data']:
            data['label'] = data['label'] + ("@lyppv")
        out["caption"]= "负锐解析"
        return out

    def ParseURL(self,url,label,min=None,max=None):
        assert "@lyppv" in label
        print("call lyp_pv.run.ParseURL("+url+","+label+","+str(min)+","+str(max)+")")
        return run.ParseURL(url,label,min,max)
        



