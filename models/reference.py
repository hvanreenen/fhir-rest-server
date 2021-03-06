#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Reference) on 2016-10-07.
#  2016, SMART Health IT.


from . import element

class Reference(element.Element):
    """ A reference from one resource to another.
    """
    
    resource_name = "Reference"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.display = None  #type: str
        """ Text alternative for the resource.
        Type `str`. """
        
        self.reference = None  #type: str
        """ Relative, internal or absolute URL reference.
        Type `str`. """
        
        super(Reference, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(Reference, self).elementProperties()
        js.extend([
            ("display", "display", str, False, None, False),
            ("reference", "reference", str, False, None, False),
        ])
        return js


