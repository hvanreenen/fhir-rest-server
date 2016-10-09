#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class QuestionnaireResponse(domainresource.DomainResource):
    """ A structured set of questions and their answers.
    
    A structured set of questions and their answers. The questions are ordered
    and grouped into coherent subsets, corresponding to the structure of the
    grouping of the underlying questions.
    """
    
    resource_name = "QuestionnaireResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None  #type: fhirreference.FHIRReference
        """ Person who received and recorded the answers.
        Type `FHIRReference` referencing `Device, Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.authored = None  #type: fhirdate.FHIRDate
        """ Date this version was authored.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.encounter = None  #type: fhirreference.FHIRReference
        """ Primary encounter during which the answers were collected.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.group = None  #type: QuestionnaireResponseGroup
        """ Grouped questions.
        Type `QuestionnaireResponseGroup` (represented as `dict` in JSON). """
        
        self.identifier = None  #type: identifier.Identifier
        """ Unique id for this set of answers.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.questionnaire = None  #type: fhirreference.FHIRReference
        """ Form being answered.
        Type `FHIRReference` referencing `Questionnaire` (represented as `dict` in JSON). """
        
        self.source = None  #type: fhirreference.FHIRReference
        """ The person who answered the questions.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.status = None  #type: str
        """ in-progress | completed | amended.
        Type `str`. """
        
        self.subject = None  #type: fhirreference.FHIRReference
        """ The subject of the questions.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(QuestionnaireResponse, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(QuestionnaireResponse, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authored", "authored", fhirdate.FHIRDate, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("group", "group", QuestionnaireResponseGroup, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("questionnaire", "questionnaire", fhirreference.FHIRReference, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class QuestionnaireResponseGroup(backboneelement.BackboneElement):
    """ Grouped questions.
    
    A group of questions to a possibly similarly grouped set of questions in
    the questionnaire response.
    """
    
    resource_name = "QuestionnaireResponseGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.group = None  #type: QuestionnaireResponseGroup
        """ Nested questionnaire response group.
        List of `QuestionnaireResponseGroup` items (represented as `dict` in JSON). """
        
        self.linkId = None  #type: str
        """ Corresponding group within Questionnaire.
        Type `str`. """
        
        self.question = None  #type: QuestionnaireResponseGroupQuestion
        """ Questions in this group.
        List of `QuestionnaireResponseGroupQuestion` items (represented as `dict` in JSON). """
        
        self.subject = None  #type: fhirreference.FHIRReference
        """ The subject this group's answers are about.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.text = None  #type: str
        """ Additional text for the group.
        Type `str`. """
        
        self.title = None  #type: str
        """ Name for this group.
        Type `str`. """
        
        super(QuestionnaireResponseGroup, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(QuestionnaireResponseGroup, self).elementProperties()
        js.extend([
            ("group", "group", QuestionnaireResponseGroup, True, None, False),
            ("linkId", "linkId", str, False, None, False),
            ("question", "question", QuestionnaireResponseGroupQuestion, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("text", "text", str, False, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js


class QuestionnaireResponseGroupQuestion(backboneelement.BackboneElement):
    """ Questions in this group.
    
    Set of questions within this group. The order of questions within the group
    is relevant.
    """
    
    resource_name = "QuestionnaireResponseGroupQuestion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answer = None  #type: QuestionnaireResponseGroupQuestionAnswer
        """ The response(s) to the question.
        List of `QuestionnaireResponseGroupQuestionAnswer` items (represented as `dict` in JSON). """
        
        self.linkId = None  #type: str
        """ Corresponding question within Questionnaire.
        Type `str`. """
        
        self.text = None  #type: str
        """ Text of the question as it is shown to the user.
        Type `str`. """
        
        super(QuestionnaireResponseGroupQuestion, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(QuestionnaireResponseGroupQuestion, self).elementProperties()
        js.extend([
            ("answer", "answer", QuestionnaireResponseGroupQuestionAnswer, True, None, False),
            ("linkId", "linkId", str, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


class QuestionnaireResponseGroupQuestionAnswer(backboneelement.BackboneElement):
    """ The response(s) to the question.
    
    The respondent's answer(s) to the question.
    """
    
    resource_name = "QuestionnaireResponseGroupQuestionAnswer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.group = None  #type: QuestionnaireResponseGroup
        """ Nested questionnaire group.
        List of `QuestionnaireResponseGroup` items (represented as `dict` in JSON). """
        
        self.valueAttachment = None  #type: attachment.Attachment
        """ Single-valued answer to the question.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBoolean = None  #type: bool
        """ Single-valued answer to the question.
        Type `bool`. """
        
        self.valueCoding = None  #type: coding.Coding
        """ Single-valued answer to the question.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDate = None  #type: fhirdate.FHIRDate
        """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None  #type: fhirdate.FHIRDate
        """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None  #type: float
        """ Single-valued answer to the question.
        Type `float`. """
        
        self.valueInstant = None  #type: fhirdate.FHIRDate
        """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None  #type: int
        """ Single-valued answer to the question.
        Type `int`. """
        
        self.valueQuantity = None  #type: quantity.Quantity
        """ Single-valued answer to the question.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference = None  #type: fhirreference.FHIRReference
        """ Single-valued answer to the question.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.valueString = None  #type: str
        """ Single-valued answer to the question.
        Type `str`. """
        
        self.valueTime = None  #type: fhirdate.FHIRDate
        """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueUri = None  #type: str
        """ Single-valued answer to the question.
        Type `str`. """
        
        super(QuestionnaireResponseGroupQuestionAnswer, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(QuestionnaireResponseGroupQuestionAnswer, self).elementProperties()
        js.extend([
            ("group", "group", QuestionnaireResponseGroup, True, None, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
        ])
        return js


from . import attachment
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
