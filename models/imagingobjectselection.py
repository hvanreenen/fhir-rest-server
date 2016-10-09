#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ImagingObjectSelection) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class ImagingObjectSelection(domainresource.DomainResource):
    """ Key Object Selection.
    
    A manifest of a set of DICOM Service-Object Pair Instances (SOP Instances).
    The referenced SOP Instances (images or other content) are for a single
    patient, and may be from one or more studies. The referenced SOP Instances
    have been selected for a purpose, such as quality assurance, conference, or
    consult. Reflecting that range of purposes, typical ImagingObjectSelection
    resources may include all SOP Instances in a study (perhaps for sharing
    through a Health Information Exchange); key images from multiple studies
    (for reference by a referring or treating physician); a multi-frame
    ultrasound instance ("cine" video clip) and a set of measurements taken
    from that instance (for inclusion in a teaching file); and so on.
    """
    
    resource_name = "ImagingObjectSelection"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None  #type: fhirreference.FHIRReference
        """ Author (human or machine).
        Type `FHIRReference` referencing `Practitioner, Device, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.authoringTime = None  #type: fhirdate.FHIRDate
        """ Authoring time of the selection.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None  #type: str
        """ Description text.
        Type `str`. """
        
        self.patient = None  #type: fhirreference.FHIRReference
        """ Patient of the selected objects.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.study = None  #type: ImagingObjectSelectionStudy
        """ Study identity of the selected instances.
        List of `ImagingObjectSelectionStudy` items (represented as `dict` in JSON). """
        
        self.title = None  #type: codeableconcept.CodeableConcept
        """ Reason for selection.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.uid = None  #type: str
        """ Instance UID.
        Type `str`. """
        
        super(ImagingObjectSelection, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ImagingObjectSelection, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authoringTime", "authoringTime", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("study", "study", ImagingObjectSelectionStudy, True, None, True),
            ("title", "title", codeableconcept.CodeableConcept, False, None, True),
            ("uid", "uid", str, False, None, True),
        ])
        return js


from . import backboneelement

class ImagingObjectSelectionStudy(backboneelement.BackboneElement):
    """ Study identity of the selected instances.
    
    Study identity and locating information of the DICOM SOP instances in the
    selection.
    """
    
    resource_name = "ImagingObjectSelectionStudy"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.imagingStudy = None  #type: fhirreference.FHIRReference
        """ Reference to ImagingStudy.
        Type `FHIRReference` referencing `ImagingStudy` (represented as `dict` in JSON). """
        
        self.series = None  #type: ImagingObjectSelectionStudySeries
        """ Series identity of the selected instances.
        List of `ImagingObjectSelectionStudySeries` items (represented as `dict` in JSON). """
        
        self.uid = None  #type: str
        """ Study instance UID.
        Type `str`. """
        
        self.url = None  #type: str
        """ Retrieve study URL.
        Type `str`. """
        
        super(ImagingObjectSelectionStudy, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ImagingObjectSelectionStudy, self).elementProperties()
        js.extend([
            ("imagingStudy", "imagingStudy", fhirreference.FHIRReference, False, None, False),
            ("series", "series", ImagingObjectSelectionStudySeries, True, None, True),
            ("uid", "uid", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


class ImagingObjectSelectionStudySeries(backboneelement.BackboneElement):
    """ Series identity of the selected instances.
    
    Series identity and locating information of the DICOM SOP instances in the
    selection.
    """
    
    resource_name = "ImagingObjectSelectionStudySeries"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.instance = None  #type: ImagingObjectSelectionStudySeriesInstance
        """ The selected instance.
        List of `ImagingObjectSelectionStudySeriesInstance` items (represented as `dict` in JSON). """
        
        self.uid = None  #type: str
        """ Series instance UID.
        Type `str`. """
        
        self.url = None  #type: str
        """ Retrieve series URL.
        Type `str`. """
        
        super(ImagingObjectSelectionStudySeries, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ImagingObjectSelectionStudySeries, self).elementProperties()
        js.extend([
            ("instance", "instance", ImagingObjectSelectionStudySeriesInstance, True, None, True),
            ("uid", "uid", str, False, None, False),
            ("url", "url", str, False, None, False),
        ])
        return js


class ImagingObjectSelectionStudySeriesInstance(backboneelement.BackboneElement):
    """ The selected instance.
    
    Identity and locating information of the selected DICOM SOP instances.
    """
    
    resource_name = "ImagingObjectSelectionStudySeriesInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.frames = None  #type: ImagingObjectSelectionStudySeriesInstanceFrames
        """ The frame set.
        List of `ImagingObjectSelectionStudySeriesInstanceFrames` items (represented as `dict` in JSON). """
        
        self.sopClass = None  #type: str
        """ SOP class UID of instance.
        Type `str`. """
        
        self.uid = None  #type: str
        """ Selected instance UID.
        Type `str`. """
        
        self.url = None  #type: str
        """ Retrieve instance URL.
        Type `str`. """
        
        super(ImagingObjectSelectionStudySeriesInstance, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ImagingObjectSelectionStudySeriesInstance, self).elementProperties()
        js.extend([
            ("frames", "frames", ImagingObjectSelectionStudySeriesInstanceFrames, True, None, False),
            ("sopClass", "sopClass", str, False, None, True),
            ("uid", "uid", str, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


class ImagingObjectSelectionStudySeriesInstanceFrames(backboneelement.BackboneElement):
    """ The frame set.
    
    Identity and location information of the frames in the selected instance.
    """
    
    resource_name = "ImagingObjectSelectionStudySeriesInstanceFrames"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.frameNumbers = None  #type: int
        """ Frame numbers.
        List of `int` items. """
        
        self.url = None  #type: str
        """ Retrieve frame URL.
        Type `str`. """
        
        super(ImagingObjectSelectionStudySeriesInstanceFrames, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ImagingObjectSelectionStudySeriesInstanceFrames, self).elementProperties()
        js.extend([
            ("frameNumbers", "frameNumbers", int, True, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
