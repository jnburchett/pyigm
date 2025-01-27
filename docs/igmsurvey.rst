.. highlight:: rest

******************
IGMSurvey Class
******************

.. index:: AbsSystem

Notebooks
=========

.. toctree::
   :maxdepth: 1

   Simple Examples <IGMSurvey_examples>
   LLS <LLSSurvey_examples>
   DLA <DLASystem_examples>

Overview
========

This Class is designed to organize and analyze a survey of
absorption systems (defined as AbsSystem objects).
The base class is abstract, i.e. one must instantiate
one of its flavors (e.g. Generic).

By definition, an IGMSurvey is a unique collection of
AbsSystem objects.  It is specified by the number of
systems and the references.


Instantiation
=============

The AbsSystem Class may be instantiated in a few ways.
The default sets the properties listed above::

	gensurvey = GenericIGMSurvey()

More commonly, one will instantiate with one or more IGMSystem objects::

    coord = SkyCoord(ra=123.1143*u.deg, dec=-12.4321*u.deg)
    gensys = IGMSystem('MgII', coord, 1.244, [-300,300.]*u.km/u.s, NHI=16.)
    gensys.name = 'Sys1'
    #
    coord2 = SkyCoord(ra=223.1143*u.deg, dec=42.4321*u.deg)
    gensys2 = IGMSystem('MgII', coord2, 1.744, [-300,300.]*u.km/u.s, NHI=17.)
    gensys2.name = 'Sys2'
    #
    gensurvey.add_abs_sys(gensys1)
    gensurvey.add_abs_sys(gensys2)


Attributes/Properties
=====================

========   ============== ============================================
Variable   Type           Description
========   ============== ============================================
nsys       int            Number of systems in the survey
========   ============== ============================================

Sub Classes
===========

LLS
+++

Subclass for LLS survey.  Presently handles the .dat and .lst files used
by JXP.   See :doc:`LLSSurvey_examples` for more.

HDLLS DR1
---------

One can also read in the HD-LLS survey (DR1) from the internet::

   from pyigm.abssys.lls import LLSSurvey
   hdlls = LLSSurvey.load_HDLLS()


DLA
+++

Subclass for DLA survey.  Presently handles the .dat and .lst files used
by JXP.   See :doc:`DLASystem_examples` for more.

Plots
=====

Methods
=======

Output
======
