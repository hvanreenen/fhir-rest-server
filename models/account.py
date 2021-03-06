#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Account) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class Account(domainresource.DomainResource):
    """ None.
    
    A financial tool for tracking value accrued for a particular purpose.  In
    the healthcare field, used to track charges for a patient, cost centres,
    etc.
    """
    
    resource_name = "Account"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.activePeriod = None  #type: period.Period
        """ Valid from..to.
        Type `Period` (represented as `dict` in JSON). """
        
        self.balance = None  #type: quantity.Quantity
        """ How much is in account?.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.coveragePeriod = None  #type: period.Period
        """ Transaction window.
        Type `Period` (represented as `dict` in JSON). """
        
        self.currency = None  #type: coding.Coding
        """ Base currency in which balance is tracked.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.description = None  #type: str
        """ Explanation of purpose/use.
        Type `str`. """
        
        self.identifier = None  #type: identifier.Identifier
        """ Account number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None  #type: str
        """ Human-readable label.
        Type `str`. """
        
        self.owner = None  #type: fhirreference.FHIRReference
        """ Who is responsible?.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.status = None  #type: str
        """ active | inactive.
        Type `str`. """
        
        self.subject = None  #type: fhirreference.FHIRReference
        """ What is account tied to?.
        Type `FHIRReference` referencing `Patient, Device, Practitioner, Location, HealthcareService, Organization` (represented as `dict` in JSON). """
        
        self.type = None  #type: codeableconcept.CodeableConcept
        """ E.g. patient, expense, depreciation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Account, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(Account, self).elementProperties()
        js.extend([
            ("activePeriod", "activePeriod", period.Period, False, None, False),
            ("balance", "balance", quantity.Quantity, False, None, False),
            ("coveragePeriod", "coveragePeriod", period.Period, False, None, False),
            ("currency", "currency", coding.Coding, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import fhirreference
from . import identifier
from . import period
from . import quantity
