#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class PaymentReconciliation(domainresource.DomainResource):
    """ PaymentReconciliation resource.
    
    This resource provides payment details and claim references supporting a
    bulk payment.
    """
    
    resource_name = "PaymentReconciliation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None  #type: fhirdate.FHIRDate
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None  #type: PaymentReconciliationDetail
        """ Details.
        List of `PaymentReconciliationDetail` items (represented as `dict` in JSON). """
        
        self.disposition = None  #type: str
        """ Disposition Message.
        Type `str`. """
        
        self.form = None  #type: coding.Coding
        """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.identifier = None  #type: identifier.Identifier
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note = None  #type: PaymentReconciliationNote
        """ Note text.
        List of `PaymentReconciliationNote` items (represented as `dict` in JSON). """
        
        self.organization = None  #type: fhirreference.FHIRReference
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None  #type: coding.Coding
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.outcome = None  #type: str
        """ complete | error.
        Type `str`. """
        
        self.period = None  #type: period.Period
        """ Period covered.
        Type `Period` (represented as `dict` in JSON). """
        
        self.request = None  #type: fhirreference.FHIRReference
        """ Claim reference.
        Type `FHIRReference` referencing `ProcessRequest` (represented as `dict` in JSON). """
        
        self.requestOrganization = None  #type: fhirreference.FHIRReference
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestProvider = None  #type: fhirreference.FHIRReference
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.ruleset = None  #type: coding.Coding
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.total = None  #type: quantity.Quantity
        """ Total amount of Payment.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(PaymentReconciliation, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("detail", "detail", PaymentReconciliationDetail, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("form", "form", coding.Coding, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", PaymentReconciliationNote, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestOrganization", "requestOrganization", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("total", "total", quantity.Quantity, False, None, True),
        ])
        return js


from . import backboneelement

class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """ Details.
    
    List of individual settlement amounts and the corresponding transaction.
    """
    
    resource_name = "PaymentReconciliationDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None  #type: quantity.Quantity
        """ Detail amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.date = None  #type: fhirdate.FHIRDate
        """ Invoice date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.payee = None  #type: fhirreference.FHIRReference
        """ Payee.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.request = None  #type: fhirreference.FHIRReference
        """ Claim.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.responce = None  #type: fhirreference.FHIRReference
        """ Claim Response.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.submitter = None  #type: fhirreference.FHIRReference
        """ Submitter.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.type = None  #type: coding.Coding
        """ Type code.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(PaymentReconciliationDetail, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("payee", "payee", fhirreference.FHIRReference, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("responce", "responce", fhirreference.FHIRReference, False, None, False),
            ("submitter", "submitter", fhirreference.FHIRReference, False, None, False),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class PaymentReconciliationNote(backboneelement.BackboneElement):
    """ Note text.
    
    Suite of notes.
    """
    
    resource_name = "PaymentReconciliationNote"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.text = None  #type: str
        """ Notes text.
        Type `str`. """
        
        self.type = None  #type: coding.Coding
        """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(PaymentReconciliationNote, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(PaymentReconciliationNote, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
