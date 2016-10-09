#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/OperationOutcome) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class OperationOutcome(domainresource.DomainResource):
    """ Information about the success/failure of an action.
    
    A collection of error, warning or information messages that result from a
    system action.
    """
    
    resource_name = "OperationOutcome"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.issue = None  #type: OperationOutcomeIssue
        """ A single issue associated with the action.
        List of `OperationOutcomeIssue` items (represented as `dict` in JSON). """
        
        super(OperationOutcome, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(OperationOutcome, self).elementProperties()
        js.extend([
            ("issue", "issue", OperationOutcomeIssue, True, None, True),
        ])
        return js


from . import backboneelement

class OperationOutcomeIssue(backboneelement.BackboneElement):
    """ A single issue associated with the action.
    
    An error, warning or information message that results from a system action.
    """
    
    resource_name = "OperationOutcomeIssue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None  #type: str
        """ Error or warning code.
        Type `str`. """
        
        self.details = None  #type: codeableconcept.CodeableConcept
        """ Additional details about the error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diagnostics = None  #type: str
        """ Additional diagnostic information about the issue.
        Type `str`. """
        
        self.location = None  #type: str
        """ XPath of element(s) related to issue.
        List of `str` items. """
        
        self.severity = None  #type: str
        """ fatal | error | warning | information.
        Type `str`. """
        
        super(OperationOutcomeIssue, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(OperationOutcomeIssue, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("details", "details", codeableconcept.CodeableConcept, False, None, False),
            ("diagnostics", "diagnostics", str, False, None, False),
            ("location", "location", str, True, None, False),
            ("severity", "severity", str, False, None, True),
        ])
        return js


from . import codeableconcept
