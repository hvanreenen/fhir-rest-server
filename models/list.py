#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/List) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class List(domainresource.DomainResource):
    """ Information summarized from a list of other resources.
    
    A set of information summarized from a list of other resources.
    """
    
    resource_name = "List"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None  #type: codeableconcept.CodeableConcept
        """ What the purpose of this list is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None  #type: fhirdate.FHIRDate
        """ When the list was prepared.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.emptyReason = None  #type: codeableconcept.CodeableConcept
        """ Why list is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.encounter = None  #type: fhirreference.FHIRReference
        """ Context in which list created.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.entry = None  #type: ListEntry
        """ Entries in the list.
        List of `ListEntry` items (represented as `dict` in JSON). """
        
        self.identifier = None  #type: identifier.Identifier
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.mode = None  #type: str
        """ working | snapshot | changes.
        Type `str`. """
        
        self.note = None  #type: str
        """ Comments about the list.
        Type `str`. """
        
        self.orderedBy = None  #type: codeableconcept.CodeableConcept
        """ What order the list has.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None  #type: fhirreference.FHIRReference
        """ Who and/or what defined the list contents (aka Author).
        Type `FHIRReference` referencing `Practitioner, Patient, Device` (represented as `dict` in JSON). """
        
        self.status = None  #type: str
        """ current | retired | entered-in-error.
        Type `str`. """
        
        self.subject = None  #type: fhirreference.FHIRReference
        """ If all resources have the same subject.
        Type `FHIRReference` referencing `Patient, Group, Device, Location` (represented as `dict` in JSON). """
        
        self.title = None  #type: str
        """ Descriptive name for the list.
        Type `str`. """
        
        super(List, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(List, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("entry", "entry", ListEntry, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("mode", "mode", str, False, None, True),
            ("note", "note", str, False, None, False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js


from . import backboneelement

class ListEntry(backboneelement.BackboneElement):
    """ Entries in the list.
    
    Entries in this list.
    """
    
    resource_name = "ListEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None  #type: fhirdate.FHIRDate
        """ When item added to list.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deleted = None  #type: bool
        """ If this item is actually marked as deleted.
        Type `bool`. """
        
        self.flag = None  #type: codeableconcept.CodeableConcept
        """ Status/Workflow information about this item.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.item = None  #type: fhirreference.FHIRReference
        """ Actual entry.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(ListEntry, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ListEntry, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("deleted", "deleted", bool, False, None, False),
            ("flag", "flag", codeableconcept.CodeableConcept, False, None, False),
            ("item", "item", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
