# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BatchDetectLanguageSentimentsResult(object):
    """
    Result of sentiments detect call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BatchDetectLanguageSentimentsResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param documents:
            The value to assign to the documents property of this BatchDetectLanguageSentimentsResult.
        :type documents: list[oci.ai_language.models.SentimentDocumentResult]

        :param errors:
            The value to assign to the errors property of this BatchDetectLanguageSentimentsResult.
        :type errors: list[oci.ai_language.models.DocumentError]

        """
        self.swagger_types = {
            'documents': 'list[SentimentDocumentResult]',
            'errors': 'list[DocumentError]'
        }

        self.attribute_map = {
            'documents': 'documents',
            'errors': 'errors'
        }

        self._documents = None
        self._errors = None

    @property
    def documents(self):
        """
        **[Required]** Gets the documents of this BatchDetectLanguageSentimentsResult.
        List of succeeded document response.


        :return: The documents of this BatchDetectLanguageSentimentsResult.
        :rtype: list[oci.ai_language.models.SentimentDocumentResult]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this BatchDetectLanguageSentimentsResult.
        List of succeeded document response.


        :param documents: The documents of this BatchDetectLanguageSentimentsResult.
        :type: list[oci.ai_language.models.SentimentDocumentResult]
        """
        self._documents = documents

    @property
    def errors(self):
        """
        Gets the errors of this BatchDetectLanguageSentimentsResult.
        List of failed document response.


        :return: The errors of this BatchDetectLanguageSentimentsResult.
        :rtype: list[oci.ai_language.models.DocumentError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this BatchDetectLanguageSentimentsResult.
        List of failed document response.


        :param errors: The errors of this BatchDetectLanguageSentimentsResult.
        :type: list[oci.ai_language.models.DocumentError]
        """
        self._errors = errors

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
