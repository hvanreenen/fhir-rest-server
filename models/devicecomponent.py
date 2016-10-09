#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DeviceComponent) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class DeviceComponent(domainresource.DomainResource):
    """ An instance of a medical-related component of a medical device.
    
    Describes the characteristics, operational status and capabilities of a
    medical-related component of a medical device.
    """
    
    resource_name = "DeviceComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None  #type: identifier.Identifier
        """ Instance id assigned by the software stack.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.languageCode = None  #type: codeableconcept.CodeableConcept
        """ Language code for the human-readable text strings produced by the
        device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.lastSystemChange = None  #type: fhirdate.FHIRDate
        """ Recent system change timestamp.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.measurementPrinciple = None  #type: str
        """ other | chemical | electrical | impedance | nuclear | optical |
        thermal | biological | mechanical | acoustical | manual+.
        Type `str`. """
        
        self.operationalStatus = None  #type: codeableconcept.CodeableConcept
        """ Component operational status.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.parameterGroup = None  #type: codeableconcept.CodeableConcept
        """ Current supported parameter group.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.parent = None  #type: fhirreference.FHIRReference
        """ Parent resource link.
        Type `FHIRReference` referencing `DeviceComponent` (represented as `dict` in JSON). """
        
        self.productionSpecification = None  #type: DeviceComponentProductionSpecification
        """ Production specification of the component.
        List of `DeviceComponentProductionSpecification` items (represented as `dict` in JSON). """
        
        self.source = None  #type: fhirreference.FHIRReference
        """ A source device of this component.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.type = None  #type: codeableconcept.CodeableConcept
        """ What kind of component it is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceComponent, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(DeviceComponent, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("languageCode", "languageCode", codeableconcept.CodeableConcept, False, None, False),
            ("lastSystemChange", "lastSystemChange", fhirdate.FHIRDate, False, None, True),
            ("measurementPrinciple", "measurementPrinciple", str, False, None, False),
            ("operationalStatus", "operationalStatus", codeableconcept.CodeableConcept, True, None, False),
            ("parameterGroup", "parameterGroup", codeableconcept.CodeableConcept, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("productionSpecification", "productionSpecification", DeviceComponentProductionSpecification, True, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import backboneelement

class DeviceComponentProductionSpecification(backboneelement.BackboneElement):
    """ Production specification of the component.
    
    Describes the production specification such as component revision, serial
    number, etc.
    """
    
    resource_name = "DeviceComponentProductionSpecification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.componentId = None  #type: identifier.Identifier
        """ Internal component unique identification.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.productionSpec = None  #type: str
        """ A printable string defining the component.
        Type `str`. """
        
        self.specType = None  #type: codeableconcept.CodeableConcept
        """ Specification type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceComponentProductionSpecification, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(DeviceComponentProductionSpecification, self).elementProperties()
        js.extend([
            ("componentId", "componentId", identifier.Identifier, False, None, False),
            ("productionSpec", "productionSpec", str, False, None, False),
            ("specType", "specType", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
