# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220926


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmailSubmittedResponse(object):
    """
    Response object that is returned to sender upon successfully submitting the email request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EmailSubmittedResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message_id:
            The value to assign to the message_id property of this EmailSubmittedResponse.
        :type message_id: str

        :param envelope_id:
            The value to assign to the envelope_id property of this EmailSubmittedResponse.
        :type envelope_id: str

        :param suppressed_recipients:
            The value to assign to the suppressed_recipients property of this EmailSubmittedResponse.
        :type suppressed_recipients: list[oci.email_data_plane.models.EmailAddress]

        """
        self.swagger_types = {
            'message_id': 'str',
            'envelope_id': 'str',
            'suppressed_recipients': 'list[EmailAddress]'
        }

        self.attribute_map = {
            'message_id': 'messageId',
            'envelope_id': 'envelopeId',
            'suppressed_recipients': 'suppressedRecipients'
        }

        self._message_id = None
        self._envelope_id = None
        self._suppressed_recipients = None

    @property
    def message_id(self):
        """
        **[Required]** Gets the message_id of this EmailSubmittedResponse.
        The unique ID for the email's Message-ID header used for service log correlation. The submission will return an error if the syntax is not a valid RFC 5322 Message-ID. This will be generated if not provided.
        Example: sdiofu234qwermls24fd@mail.example.com


        :return: The message_id of this EmailSubmittedResponse.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """
        Sets the message_id of this EmailSubmittedResponse.
        The unique ID for the email's Message-ID header used for service log correlation. The submission will return an error if the syntax is not a valid RFC 5322 Message-ID. This will be generated if not provided.
        Example: sdiofu234qwermls24fd@mail.example.com


        :param message_id: The message_id of this EmailSubmittedResponse.
        :type: str
        """
        self._message_id = message_id

    @property
    def envelope_id(self):
        """
        **[Required]** Gets the envelope_id of this EmailSubmittedResponse.
        Email Delivery generated unique Envelope ID of the email submission. If you need to contact Email Delivery about a particular request, please provide the Envelope ID.


        :return: The envelope_id of this EmailSubmittedResponse.
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """
        Sets the envelope_id of this EmailSubmittedResponse.
        Email Delivery generated unique Envelope ID of the email submission. If you need to contact Email Delivery about a particular request, please provide the Envelope ID.


        :param envelope_id: The envelope_id of this EmailSubmittedResponse.
        :type: str
        """
        self._envelope_id = envelope_id

    @property
    def suppressed_recipients(self):
        """
        **[Required]** Gets the suppressed_recipients of this EmailSubmittedResponse.
        Return list of suppressed email addresses.


        :return: The suppressed_recipients of this EmailSubmittedResponse.
        :rtype: list[oci.email_data_plane.models.EmailAddress]
        """
        return self._suppressed_recipients

    @suppressed_recipients.setter
    def suppressed_recipients(self, suppressed_recipients):
        """
        Sets the suppressed_recipients of this EmailSubmittedResponse.
        Return list of suppressed email addresses.


        :param suppressed_recipients: The suppressed_recipients of this EmailSubmittedResponse.
        :type: list[oci.email_data_plane.models.EmailAddress]
        """
        self._suppressed_recipients = suppressed_recipients

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
