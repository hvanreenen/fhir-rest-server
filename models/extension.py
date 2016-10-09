#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Extension) on 2016-10-07.
#  2016, SMART Health IT.


from . import element

class Extension(element.Element):
    """ None.
    
    Optional Extensions Element - found in all resources.
    """
    
    resource_name = "Extension"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None  #type: str
        """ identifies the meaning of the extension.
        Type `str`. """
        
        self.valueAddress = None  #type: address.Address
        """ Value of extension.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None  #type: annotation.Annotation
        """ Value of extension.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None  #type: attachment.Attachment
        """ Value of extension.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None  #type: str
        """ Value of extension.
        Type `str`. """
        
        self.valueBoolean = None  #type: bool
        """ Value of extension.
        Type `bool`. """
        
        self.valueCode = None  #type: str
        """ Value of extension.
        Type `str`. """
        
        self.valueCodeableConcept = None  #type: codeableconcept.CodeableConcept
        """ Value of extension.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None  #type: coding.Coding
        """ Value of extension.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None  #type: contactpoint.ContactPoint
        """ Value of extension.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueDate = None  #type: fhirdate.FHIRDate
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None  #type: fhirdate.FHIRDate
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None  #type: float
        """ Value of extension.
        Type `float`. """
        
        self.valueHumanName = None  #type: humanname.HumanName
        """ Value of extension.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId = None  #type: str
        """ Value of extension.
        Type `str`. """
        
        self.valueIdentifier = None  #type: identifier.Identifier
        """ Value of extension.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None  #type: fhirdate.FHIRDate
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None  #type: int
        """ Value of extension.
        Type `int`. """
        
        self.valueMarkdown = None  #type: str
        """ Value of extension.
        Type `str`. """
        
        self.valueMeta = None  #type: meta.Meta
        """ Value of extension.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.valueOid = None  #type: str
        """ Value of extension.
        Type `str`. """
        
        self.valuePeriod = None  #type: period.Period
        """ Value of extension.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt = None  #type: int
        """ Value of extension.
        Type `int`. """
        
        self.valueQuantity = None  #type: quantity.Quantity
        """ Value of extension.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None  #type: range.Range
        """ Value of extension.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None  #type: ratio.Ratio
        """ Value of extension.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None  #type: fhirreference.FHIRReference
        """ Value of extension.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueSampledData = None  #type: sampleddata.SampledData
        """ Value of extension.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None  #type: signature.Signature
        """ Value of extension.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None  #type: str
        """ Value of extension.
        Type `str`. """
        
        self.valueTime = None  #type: fhirdate.FHIRDate
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None  #type: timing.Timing
        """ Value of extension.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt = None  #type: int
        """ Value of extension.
        Type `int`. """
        
        self.valueUri = None  #type: str
        """ Value of extension.
        Type `str`. """
        
        super(Extension, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(Extension, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", False),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCode", "valueCode", str, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", False),
            ("valueId", "valueId", str, False, "value", False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", False),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", False),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", False),
            ("valueOid", "valueOid", str, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", False),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
        ])
        return js


from . import address
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import meta
from . import period
from . import quantity
from . import range
from . import ratio
from . import sampleddata
from . import signature
from . import timing
