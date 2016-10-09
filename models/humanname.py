#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/HumanName) on 2016-10-07.
#  2016, SMART Health IT.


from . import element

class HumanName(element.Element):
    """ Name of a human - parts and usage.
    
    A human's name with the ability to identify parts and usage.
    """
    
    resource_name = "HumanName"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.family = None  #type: str
        """ Family name (often called 'Surname').
        List of `str` items. """
        
        self.given = None  #type: str
        """ Given names (not always 'first'). Includes middle names.
        List of `str` items. """
        
        self.period = None  #type: period.Period
        """ Time period when name was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.prefix = None  #type: str
        """ Parts that come before the name.
        List of `str` items. """
        
        self.suffix = None  #type: str
        """ Parts that come after the name.
        List of `str` items. """
        
        self.text = None  #type: str
        """ Text representation of the full name.
        Type `str`. """
        
        self.use = None  #type: str
        """ usual | official | temp | nickname | anonymous | old | maiden.
        Type `str`. """
        
        super(HumanName, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(HumanName, self).elementProperties()
        js.extend([
            ("family", "family", str, True, None, False),
            ("given", "given", str, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("prefix", "prefix", str, True, None, False),
            ("suffix", "suffix", str, True, None, False),
            ("text", "text", str, False, None, False),
            ("use", "use", str, False, None, False),
        ])
        return js


from . import period
