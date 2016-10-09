#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Attachment) on 2016-10-07.
#  2016, SMART Health IT.


from . import element

class Attachment(element.Element):
    """ Content in a format defined elsewhere.
    
    For referring to data content defined in other formats.
    """
    
    resource_name = "Attachment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentType = None  #type: str
        """ Mime type of the content, with charset etc..
        Type `str`. """
        
        self.creation = None  #type: fhirdate.FHIRDate
        """ Date attachment was first created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.data = None  #type: str
        """ Data inline, base64ed.
        Type `str`. """
        
        self.hash = None  #type: str
        """ Hash of the data (sha-1, base64ed).
        Type `str`. """
        
        self.language = None  #type: str
        """ Human language of the content (BCP-47).
        Type `str`. """
        
        self.size = None  #type: int
        """ Number of bytes of content (if url provided).
        Type `int`. """
        
        self.title = None  #type: str
        """ Label to display in place of the data.
        Type `str`. """
        
        self.url = None  #type: str
        """ Uri where the data can be found.
        Type `str`. """
        
        super(Attachment, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(Attachment, self).elementProperties()
        js.extend([
            ("contentType", "contentType", str, False, None, False),
            ("creation", "creation", fhirdate.FHIRDate, False, None, False),
            ("data", "data", str, False, None, False),
            ("hash", "hash", str, False, None, False),
            ("language", "language", str, False, None, False),
            ("size", "size", int, False, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
        ])
        return js


from . import fhirdate
