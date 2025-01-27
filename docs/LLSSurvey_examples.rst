
Examples for LLSSurvey (v1.2)
=============================

.. code:: python

    # imports
    #from xastropy.igm.abs_sys import lls_utils as llsu
    from pyigm.abssys.lls import LLSSurvey
    
    import urllib2, urllib
    import imp, json
    
    xa_path = imp.find_module('xastropy')[1]
    if xa_path is None:
        raise ValueError("Requires xastropy for now")

Instantiate
-----------

LLS Tree (JXP) -- Likely to Deprecate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    #reload(llsu)
    lls_survey = LLSSurvey.from_flist('Lists/lls_metals.lst', tree=os.getenv('LLSTREE'))


.. parsed-literal::

    Read 165 files from Lists/lls_metals.lst in the tree /u/xavier/LLS/


FITS and JSON files (HD-LLS, DR1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    # Grabs HD-LLS files from the website, as needed
    hdlls = LLSSurvey.load_HDLLS()


.. parsed-literal::

    LLSSurvey: Grabbing summary file from http://www.ucolick.org/~xavier/HD-LLS/DR1/HD-LLS_DR1.fits


::


    ---------------------------------------------------------------------------

    URLError                                  Traceback (most recent call last)

    <ipython-input-3-cd533e38f101> in <module>()
          1 # Grabs HD-LLS files from the website, as needed
    ----> 2 hdlls = LLSSurvey.load_HDLLS()
    

    /Users/xavier/local/Python/pyigm/pyigm/abssys/lls.pyc in load_HDLLS(cls)
        443             url = 'http://www.ucolick.org/~xavier/HD-LLS/DR1/HD-LLS_DR1.fits'
        444             print('LLSSurvey: Grabbing summary file from {:s}'.format(url))
    --> 445             f = urllib2.urlopen(url)
        446             summ_fil = lt_path+"/data/HD-LLS_DR1.fits"
        447             with open(summ_fil, "wb") as code:


    /Users/xavier/anaconda/lib/python2.7/urllib2.pyc in urlopen(url, data, timeout, cafile, capath, cadefault, context)
        152     else:
        153         opener = _opener
    --> 154     return opener.open(url, data, timeout)
        155 
        156 def install_opener(opener):


    /Users/xavier/anaconda/lib/python2.7/urllib2.pyc in open(self, fullurl, data, timeout)
        429             req = meth(req)
        430 
    --> 431         response = self._open(req, data)
        432 
        433         # post-process response


    /Users/xavier/anaconda/lib/python2.7/urllib2.pyc in _open(self, req, data)
        447         protocol = req.get_type()
        448         result = self._call_chain(self.handle_open, protocol, protocol +
    --> 449                                   '_open', req)
        450         if result:
        451             return result


    /Users/xavier/anaconda/lib/python2.7/urllib2.pyc in _call_chain(self, chain, kind, meth_name, *args)
        407             func = getattr(handler, meth_name)
        408 
    --> 409             result = func(*args)
        410             if result is not None:
        411                 return result


    /Users/xavier/anaconda/lib/python2.7/urllib2.pyc in http_open(self, req)
       1225 
       1226     def http_open(self, req):
    -> 1227         return self.do_open(httplib.HTTPConnection, req)
       1228 
       1229     http_request = AbstractHTTPHandler.do_request_


    /Users/xavier/anaconda/lib/python2.7/urllib2.pyc in do_open(self, http_class, req, **http_conn_args)
       1195         except socket.error, err: # XXX what error?
       1196             h.close()
    -> 1197             raise URLError(err)
       1198         else:
       1199             try:


    URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>


Simple Attributes
-----------------

.. code:: python

    hdlls.nsys




.. parsed-literal::

    157



.. code:: python

    hdlls.NHI[0:10]




.. parsed-literal::

    array([ 19.65,  20.05,  17.55,  19.1 ,  20.  ,  19.1 ,  19.05,  19.05,
            19.25,  20.2 ])



.. code:: python

    hdlls.name[0:5]




.. parsed-literal::

    array(['HD-LLS_J000345.00-232346.5_z2.187',
           'HD-LLS_J003454.80+163920.0_z3.754',
           'HD-LLS_J004049.50-402514.0_z2.816',
           'HD-LLS_J010355.30-300946.0_z2.908',
           'HD-LLS_J010516.80-184642.0_z2.927'], 
          dtype='|S33')



.. code:: python

    CII_clms = hdlls.ions((6,2))
    CII_clms




.. raw:: html

    &lt;Table length=157&gt;
    <table id="table4526397712">
    <thead><tr><th>name</th><th>logN</th><th>sig_logN</th><th>flg_inst</th><th>ion</th><th>Z</th><th>flag_N</th></tr></thead>
    <thead><tr><th>unicode32</th><th>float64</th><th>float64</th><th>int64</th><th>int64</th><th>int64</th><th>int64</th></tr></thead>
    <tr><td>HD-LLS_J000345.00-232346.5_z2.18</td><td>14.447</td><td>0.017</td><td>144</td><td>2</td><td>6</td><td>2</td></tr>
    <tr><td>HD-LLS_J003454.80+163920.0_z3.75</td><td>0.0</td><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>HD-LLS_J004049.50-402514.0_z2.81</td><td>13.421</td><td>0.0</td><td>8</td><td>2</td><td>6</td><td>3</td></tr>
    <tr><td>HD-LLS_J010355.30-300946.0_z2.90</td><td>13.901</td><td>0.03</td><td>144</td><td>2</td><td>6</td><td>1</td></tr>
    <tr><td>HD-LLS_J010516.80-184642.0_z2.92</td><td>14.594</td><td>0.016</td><td>8</td><td>2</td><td>6</td><td>2</td></tr>
    <tr><td>HD-LLS_J010619.24+004823.3_z3.32</td><td>0.0</td><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>HD-LLS_J010619.24+004823.3_z4.17</td><td>0.0</td><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>HD-LLS_J010619.24+004823.3_z3.28</td><td>0.0</td><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>HD-LLS_J012156.03+144823.8_z2.66</td><td>14.794</td><td>0.02</td><td>1</td><td>2</td><td>6</td><td>2</td></tr>
    <tr><td>HD-LLS_J012403.80+004432.7_z3.07</td><td>0.0</td><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
    <tr><td>HD-LLS_J231543.56+145606.0_z2.94</td><td>0.0</td><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>HD-LLS_J231543.56+145606.0_z3.13</td><td>13.71</td><td>0.027</td><td>1</td><td>2</td><td>6</td><td>1</td></tr>
    <tr><td>HD-LLS_J231643.20-334912.0_z2.38</td><td>0.0</td><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>HD-LLS_J231934.77-104036.9_z2.67</td><td>0.0</td><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>HD-LLS_J232340.90+275800.0_z3.26</td><td>0.0</td><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>HD-LLS_J232340.90+275800.0_z3.56</td><td>0.0</td><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>HD-LLS_J233446.40-090812.3_z3.22</td><td>12.746</td><td>0.078</td><td>1</td><td>2</td><td>6</td><td>1</td></tr>
    <tr><td>HD-LLS_J234855.40-144436.6_z2.77</td><td>13.027</td><td>0.104</td><td>144</td><td>2</td><td>6</td><td>1</td></tr>
    <tr><td>HD-LLS_J235057.87-005209.9_z2.93</td><td>14.004</td><td>0.038</td><td>8</td><td>2</td><td>6</td><td>1</td></tr>
    <tr><td>HD-LLS_J235833.50-544042.0_z2.89</td><td>13.428</td><td>0.092</td><td>144</td><td>2</td><td>6</td><td>1</td></tr>
    </table>



