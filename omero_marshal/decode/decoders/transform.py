#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from ... import SCHEMA_VERSION
from .annotation import Decoder
try:
    from omero.model import AffineTransformI
except ImportError:
    from omero_marshal.legacy import AffineTransformI
from omero.rtypes import rdouble


class Transform201501Decoder(Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#AffineTransform'

    OMERO_CLASS = AffineTransformI


class Transform201606Decoder(Transform201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#AffineTransform'

    def decode(self, data):
        t = super(Transform201606Decoder, self).decode(data)
        t.setA00(rdouble(data['A00']))
        t.setA10(rdouble(data['A10']))
        t.setA01(rdouble(data['A01']))
        t.setA11(rdouble(data['A11']))
        t.setA02(rdouble(data['A02']))
        t.setA12(rdouble(data['A12']))
        return t


if SCHEMA_VERSION == '2015-01':
    decoder = (Transform201501Decoder.TYPE, Transform201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Transform201606Decoder.TYPE, Transform201606Decoder)
TransformDecoder = decoder[1]
