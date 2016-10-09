#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Claim) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.
    
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """
    
    resource_name = "Claim"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accident = None  #type: fhirdate.FHIRDate
        """ Accident Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.accidentType = None  #type: coding.Coding
        """ Accident Type.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.additionalMaterials = None  #type: coding.Coding
        """ Additional materials, documents, etc..
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.condition = None  #type: coding.Coding
        """ List of presenting Conditions.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.coverage = None  #type: ClaimCoverage
        """ Insurance or medical plan.
        List of `ClaimCoverage` items (represented as `dict` in JSON). """
        
        self.created = None  #type: fhirdate.FHIRDate
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.diagnosis = None  #type: ClaimDiagnosis
        """ Diagnosis.
        List of `ClaimDiagnosis` items (represented as `dict` in JSON). """
        
        self.enterer = None  #type: fhirreference.FHIRReference
        """ Author.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.exception = None  #type: coding.Coding
        """ Eligibility exceptions.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.facility = None  #type: fhirreference.FHIRReference
        """ Servicing Facility.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.fundsReserve = None  #type: coding.Coding
        """ Funds requested to be reserved.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.identifier = None  #type: identifier.Identifier
        """ Claim number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.interventionException = None  #type: coding.Coding
        """ Intervention and exception code (Pharma).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.item = None  #type: ClaimItem
        """ Goods and Services.
        List of `ClaimItem` items (represented as `dict` in JSON). """
        
        self.missingTeeth = None  #type: ClaimMissingTeeth
        """ Only if type = oral.
        List of `ClaimMissingTeeth` items (represented as `dict` in JSON). """
        
        self.organization = None  #type: fhirreference.FHIRReference
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalPrescription = None  #type: fhirreference.FHIRReference
        """ Original Prescription.
        Type `FHIRReference` referencing `MedicationOrder` (represented as `dict` in JSON). """
        
        self.originalRuleset = None  #type: coding.Coding
        """ Original specification followed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.patient = None  #type: fhirreference.FHIRReference
        """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.payee = None  #type: ClaimPayee
        """ Payee.
        Type `ClaimPayee` (represented as `dict` in JSON). """
        
        self.prescription = None  #type: fhirreference.FHIRReference
        """ Prescription.
        Type `FHIRReference` referencing `MedicationOrder, VisionPrescription` (represented as `dict` in JSON). """
        
        self.priority = None  #type: coding.Coding
        """ Desired processing priority.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.provider = None  #type: fhirreference.FHIRReference
        """ Responsible provider.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.referral = None  #type: fhirreference.FHIRReference
        """ Treatment Referral.
        Type `FHIRReference` referencing `ReferralRequest` (represented as `dict` in JSON). """
        
        self.ruleset = None  #type: coding.Coding
        """ Current specification followed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.school = None  #type: str
        """ Name of School.
        Type `str`. """
        
        self.target = None  #type: fhirreference.FHIRReference
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.type = None  #type: str
        """ institutional | oral | pharmacy | professional | vision.
        Type `str`. """
        
        self.use = None  #type: str
        """ complete | proposed | exploratory | other.
        Type `str`. """
        
        super(Claim, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(Claim, self).elementProperties()
        js.extend([
            ("accident", "accident", fhirdate.FHIRDate, False, None, False),
            ("accidentType", "accidentType", coding.Coding, False, None, False),
            ("additionalMaterials", "additionalMaterials", coding.Coding, True, None, False),
            ("condition", "condition", coding.Coding, True, None, False),
            ("coverage", "coverage", ClaimCoverage, True, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("diagnosis", "diagnosis", ClaimDiagnosis, True, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("exception", "exception", coding.Coding, True, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("fundsReserve", "fundsReserve", coding.Coding, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("interventionException", "interventionException", coding.Coding, True, None, False),
            ("item", "item", ClaimItem, True, None, False),
            ("missingTeeth", "missingTeeth", ClaimMissingTeeth, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, False, None, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("payee", "payee", ClaimPayee, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", coding.Coding, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("referral", "referral", fhirreference.FHIRReference, False, None, False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("school", "school", str, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
            ("use", "use", str, False, None, False),
        ])
        return js


from . import backboneelement

class ClaimCoverage(backboneelement.BackboneElement):
    """ Insurance or medical plan.
    
    Financial instrument by which payment information for health care.
    """
    
    resource_name = "ClaimCoverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.businessArrangement = None  #type: str
        """ Business agreement.
        Type `str`. """
        
        self.claimResponse = None  #type: fhirreference.FHIRReference
        """ Adjudication results.
        Type `FHIRReference` referencing `ClaimResponse` (represented as `dict` in JSON). """
        
        self.coverage = None  #type: fhirreference.FHIRReference
        """ Insurance information.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        self.focal = None  #type: bool
        """ The focal Coverage.
        Type `bool`. """
        
        self.originalRuleset = None  #type: coding.Coding
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.preAuthRef = None  #type: str
        """ Pre-Authorization/Determination Reference.
        List of `str` items. """
        
        self.relationship = None  #type: coding.Coding
        """ Patient relationship to subscriber.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.sequence = None  #type: int
        """ Service instance identifier.
        Type `int`. """
        
        super(ClaimCoverage, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ClaimCoverage, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("relationship", "relationship", coding.Coding, False, None, True),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimDiagnosis(backboneelement.BackboneElement):
    """ Diagnosis.
    
    Ordered list of patient diagnosis for which care is sought.
    """
    
    resource_name = "ClaimDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.diagnosis = None  #type: coding.Coding
        """ Patient's list of diagnosis.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.sequence = None  #type: int
        """ Sequence of diagnosis.
        Type `int`. """
        
        super(ClaimDiagnosis, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ClaimDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosis", "diagnosis", coding.Coding, False, None, True),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimItem(backboneelement.BackboneElement):
    """ Goods and Services.
    
    First tier of goods and services.
    """
    
    resource_name = "ClaimItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.bodySite = None  #type: coding.Coding
        """ Service Location.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.detail = None  #type: ClaimItemDetail
        """ Additional items.
        List of `ClaimItemDetail` items (represented as `dict` in JSON). """
        
        self.diagnosisLinkId = None  #type: int
        """ Diagnosis Link.
        List of `int` items. """
        
        self.factor = None  #type: float
        """ Price scaling factor.
        Type `float`. """
        
        self.modifier = None  #type: coding.Coding
        """ Service/Product billing modifiers.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.net = None  #type: quantity.Quantity
        """ Total item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.points = None  #type: float
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.prosthesis = None  #type: ClaimItemProsthesis
        """ Prosthetic details.
        Type `ClaimItemProsthesis` (represented as `dict` in JSON). """
        
        self.provider = None  #type: fhirreference.FHIRReference
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.quantity = None  #type: quantity.Quantity
        """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.sequence = None  #type: int
        """ Service instance.
        Type `int`. """
        
        self.service = None  #type: coding.Coding
        """ Item Code.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.serviceDate = None  #type: fhirdate.FHIRDate
        """ Date of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.subSite = None  #type: coding.Coding
        """ Service Sub-location.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None  #type: coding.Coding
        """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.udi = None  #type: coding.Coding
        """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.unitPrice = None  #type: quantity.Quantity
        """ Fee, charge or cost per point.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(ClaimItem, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ClaimItem, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", coding.Coding, False, None, False),
            ("detail", "detail", ClaimItemDetail, True, None, False),
            ("diagnosisLinkId", "diagnosisLinkId", int, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", coding.Coding, True, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("points", "points", float, False, None, False),
            ("prosthesis", "prosthesis", ClaimItemProsthesis, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("serviceDate", "serviceDate", fhirdate.FHIRDate, False, None, False),
            ("subSite", "subSite", coding.Coding, True, None, False),
            ("type", "type", coding.Coding, False, None, True),
            ("udi", "udi", coding.Coding, False, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
        ])
        return js


class ClaimItemDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Second tier of goods and services.
    """
    
    resource_name = "ClaimItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.factor = None  #type: float
        """ Price scaling factor.
        Type `float`. """
        
        self.net = None  #type: quantity.Quantity
        """ Total additional item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.points = None  #type: float
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.quantity = None  #type: quantity.Quantity
        """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.sequence = None  #type: int
        """ Service instance.
        Type `int`. """
        
        self.service = None  #type: coding.Coding
        """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subDetail = None  #type: ClaimItemDetailSubDetail
        """ Additional items.
        List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.type = None  #type: coding.Coding
        """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.udi = None  #type: coding.Coding
        """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.unitPrice = None  #type: quantity.Quantity
        """ Fee, charge or cost per point.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(ClaimItemDetail, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ClaimItemDetail, self).elementProperties()
        js.extend([
            ("factor", "factor", float, False, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("subDetail", "subDetail", ClaimItemDetailSubDetail, True, None, False),
            ("type", "type", coding.Coding, False, None, True),
            ("udi", "udi", coding.Coding, False, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
        ])
        return js


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Third tier of goods and services.
    """
    
    resource_name = "ClaimItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.factor = None  #type: float
        """ Price scaling factor.
        Type `float`. """
        
        self.net = None  #type: quantity.Quantity
        """ Net additional item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.points = None  #type: float
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.quantity = None  #type: quantity.Quantity
        """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.sequence = None  #type: int
        """ Service instance.
        Type `int`. """
        
        self.service = None  #type: coding.Coding
        """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.type = None  #type: coding.Coding
        """ Type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.udi = None  #type: coding.Coding
        """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.unitPrice = None  #type: quantity.Quantity
        """ Fee, charge or cost per point.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(ClaimItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ClaimItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("factor", "factor", float, False, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("type", "type", coding.Coding, False, None, True),
            ("udi", "udi", coding.Coding, False, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
        ])
        return js


class ClaimItemProsthesis(backboneelement.BackboneElement):
    """ Prosthetic details.
    
    The materials and placement date of prior fixed prosthesis.
    """
    
    resource_name = "ClaimItemProsthesis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.initial = None  #type: bool
        """ Is this the initial service.
        Type `bool`. """
        
        self.priorDate = None  #type: fhirdate.FHIRDate
        """ Initial service Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.priorMaterial = None  #type: coding.Coding
        """ Prosthetic Material.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimItemProsthesis, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ClaimItemProsthesis, self).elementProperties()
        js.extend([
            ("initial", "initial", bool, False, None, False),
            ("priorDate", "priorDate", fhirdate.FHIRDate, False, None, False),
            ("priorMaterial", "priorMaterial", coding.Coding, False, None, False),
        ])
        return js


class ClaimMissingTeeth(backboneelement.BackboneElement):
    """ Only if type = oral.
    
    A list of teeth which would be expected but are not found due to having
    been previously  extracted or for other reasons.
    """
    
    resource_name = "ClaimMissingTeeth"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.extractionDate = None  #type: fhirdate.FHIRDate
        """ Date of Extraction.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.reason = None  #type: coding.Coding
        """ Reason for missing.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.tooth = None  #type: coding.Coding
        """ Tooth Code.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimMissingTeeth, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ClaimMissingTeeth, self).elementProperties()
        js.extend([
            ("extractionDate", "extractionDate", fhirdate.FHIRDate, False, None, False),
            ("reason", "reason", coding.Coding, False, None, False),
            ("tooth", "tooth", coding.Coding, False, None, True),
        ])
        return js


class ClaimPayee(backboneelement.BackboneElement):
    """ Payee.
    
    The party to be reimbursed for the services.
    """
    
    resource_name = "ClaimPayee"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.organization = None  #type: fhirreference.FHIRReference
        """ Organization who is the payee.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.person = None  #type: fhirreference.FHIRReference
        """ Other person who is the payee.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.provider = None  #type: fhirreference.FHIRReference
        """ Provider who is the payee.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.type = None  #type: coding.Coding
        """ Party to be paid any benefits payable.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimPayee, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ClaimPayee, self).elementProperties()
        js.extend([
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("person", "person", fhirreference.FHIRReference, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
