# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180115


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KskDnssecKeyVersion(object):
    """
    A key signing key (KSK) version. The version information contains timing and configuration data corresponding to the KSK that is used to
    apply DNSSEC on the zone.
    """

    #: A constant which can be used with the algorithm property of a KskDnssecKeyVersion.
    #: This constant has a value of "RSASHA256"
    ALGORITHM_RSASHA256 = "RSASHA256"

    def __init__(self, **kwargs):
        """
        Initializes a new KskDnssecKeyVersion object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param uuid:
            The value to assign to the uuid property of this KskDnssecKeyVersion.
        :type uuid: str

        :param algorithm:
            The value to assign to the algorithm property of this KskDnssecKeyVersion.
            Allowed values for this property are: "RSASHA256", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type algorithm: str

        :param length_in_bytes:
            The value to assign to the length_in_bytes property of this KskDnssecKeyVersion.
        :type length_in_bytes: int

        :param time_created:
            The value to assign to the time_created property of this KskDnssecKeyVersion.
        :type time_created: datetime

        :param time_published:
            The value to assign to the time_published property of this KskDnssecKeyVersion.
        :type time_published: datetime

        :param time_activated:
            The value to assign to the time_activated property of this KskDnssecKeyVersion.
        :type time_activated: datetime

        :param time_inactivated:
            The value to assign to the time_inactivated property of this KskDnssecKeyVersion.
        :type time_inactivated: datetime

        :param time_unpublished:
            The value to assign to the time_unpublished property of this KskDnssecKeyVersion.
        :type time_unpublished: datetime

        :param time_expired:
            The value to assign to the time_expired property of this KskDnssecKeyVersion.
        :type time_expired: datetime

        :param time_promoted:
            The value to assign to the time_promoted property of this KskDnssecKeyVersion.
        :type time_promoted: datetime

        :param predecessor_dnssec_key_version_uuid:
            The value to assign to the predecessor_dnssec_key_version_uuid property of this KskDnssecKeyVersion.
        :type predecessor_dnssec_key_version_uuid: str

        :param successor_dnssec_key_version_uuid:
            The value to assign to the successor_dnssec_key_version_uuid property of this KskDnssecKeyVersion.
        :type successor_dnssec_key_version_uuid: str

        :param key_tag:
            The value to assign to the key_tag property of this KskDnssecKeyVersion.
        :type key_tag: int

        :param ds_data:
            The value to assign to the ds_data property of this KskDnssecKeyVersion.
        :type ds_data: list[oci.dns.models.DnssecKeyVersionDsData]

        """
        self.swagger_types = {
            'uuid': 'str',
            'algorithm': 'str',
            'length_in_bytes': 'int',
            'time_created': 'datetime',
            'time_published': 'datetime',
            'time_activated': 'datetime',
            'time_inactivated': 'datetime',
            'time_unpublished': 'datetime',
            'time_expired': 'datetime',
            'time_promoted': 'datetime',
            'predecessor_dnssec_key_version_uuid': 'str',
            'successor_dnssec_key_version_uuid': 'str',
            'key_tag': 'int',
            'ds_data': 'list[DnssecKeyVersionDsData]'
        }

        self.attribute_map = {
            'uuid': 'uuid',
            'algorithm': 'algorithm',
            'length_in_bytes': 'lengthInBytes',
            'time_created': 'timeCreated',
            'time_published': 'timePublished',
            'time_activated': 'timeActivated',
            'time_inactivated': 'timeInactivated',
            'time_unpublished': 'timeUnpublished',
            'time_expired': 'timeExpired',
            'time_promoted': 'timePromoted',
            'predecessor_dnssec_key_version_uuid': 'predecessorDnssecKeyVersionUuid',
            'successor_dnssec_key_version_uuid': 'successorDnssecKeyVersionUuid',
            'key_tag': 'keyTag',
            'ds_data': 'dsData'
        }

        self._uuid = None
        self._algorithm = None
        self._length_in_bytes = None
        self._time_created = None
        self._time_published = None
        self._time_activated = None
        self._time_inactivated = None
        self._time_unpublished = None
        self._time_expired = None
        self._time_promoted = None
        self._predecessor_dnssec_key_version_uuid = None
        self._successor_dnssec_key_version_uuid = None
        self._key_tag = None
        self._ds_data = None

    @property
    def uuid(self):
        """
        Gets the uuid of this KskDnssecKeyVersion.
        The UUID of the `DnssecKeyVersion`.


        :return: The uuid of this KskDnssecKeyVersion.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this KskDnssecKeyVersion.
        The UUID of the `DnssecKeyVersion`.


        :param uuid: The uuid of this KskDnssecKeyVersion.
        :type: str
        """
        self._uuid = uuid

    @property
    def algorithm(self):
        """
        Gets the algorithm of this KskDnssecKeyVersion.
        The signing algorithm used for the key.

        Allowed values for this property are: "RSASHA256", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The algorithm of this KskDnssecKeyVersion.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """
        Sets the algorithm of this KskDnssecKeyVersion.
        The signing algorithm used for the key.


        :param algorithm: The algorithm of this KskDnssecKeyVersion.
        :type: str
        """
        allowed_values = ["RSASHA256"]
        if not value_allowed_none_or_none_sentinel(algorithm, allowed_values):
            algorithm = 'UNKNOWN_ENUM_VALUE'
        self._algorithm = algorithm

    @property
    def length_in_bytes(self):
        """
        Gets the length_in_bytes of this KskDnssecKeyVersion.
        The length of the corresponding private key in bytes, expressed as an integer.


        :return: The length_in_bytes of this KskDnssecKeyVersion.
        :rtype: int
        """
        return self._length_in_bytes

    @length_in_bytes.setter
    def length_in_bytes(self, length_in_bytes):
        """
        Sets the length_in_bytes of this KskDnssecKeyVersion.
        The length of the corresponding private key in bytes, expressed as an integer.


        :param length_in_bytes: The length_in_bytes of this KskDnssecKeyVersion.
        :type: int
        """
        self._length_in_bytes = length_in_bytes

    @property
    def time_created(self):
        """
        Gets the time_created of this KskDnssecKeyVersion.
        The date and time the key version was created, expressed in RFC 3339 timestamp format.

        **Example:** `2016-07-22T17:23:59:00Z`


        :return: The time_created of this KskDnssecKeyVersion.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this KskDnssecKeyVersion.
        The date and time the key version was created, expressed in RFC 3339 timestamp format.

        **Example:** `2016-07-22T17:23:59:00Z`


        :param time_created: The time_created of this KskDnssecKeyVersion.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_published(self):
        """
        Gets the time_published of this KskDnssecKeyVersion.
        The date and time the key version was, or will be, published, expressed in RFC 3339 timestamp format. This is
        when the zone contents will include a DNSKEY record corresponding to the key material.

        **Example:** `2016-07-22T17:23:59:00Z`


        :return: The time_published of this KskDnssecKeyVersion.
        :rtype: datetime
        """
        return self._time_published

    @time_published.setter
    def time_published(self, time_published):
        """
        Sets the time_published of this KskDnssecKeyVersion.
        The date and time the key version was, or will be, published, expressed in RFC 3339 timestamp format. This is
        when the zone contents will include a DNSKEY record corresponding to the key material.

        **Example:** `2016-07-22T17:23:59:00Z`


        :param time_published: The time_published of this KskDnssecKeyVersion.
        :type: datetime
        """
        self._time_published = time_published

    @property
    def time_activated(self):
        """
        Gets the time_activated of this KskDnssecKeyVersion.
        The date and time the key version went, or will go, active, expressed in RFC 3339 timestamp format. This is
        when the key material will be used to generate RRSIGs.

        **Example:** `2016-07-22T17:23:59:00Z`


        :return: The time_activated of this KskDnssecKeyVersion.
        :rtype: datetime
        """
        return self._time_activated

    @time_activated.setter
    def time_activated(self, time_activated):
        """
        Sets the time_activated of this KskDnssecKeyVersion.
        The date and time the key version went, or will go, active, expressed in RFC 3339 timestamp format. This is
        when the key material will be used to generate RRSIGs.

        **Example:** `2016-07-22T17:23:59:00Z`


        :param time_activated: The time_activated of this KskDnssecKeyVersion.
        :type: datetime
        """
        self._time_activated = time_activated

    @property
    def time_inactivated(self):
        """
        Gets the time_inactivated of this KskDnssecKeyVersion.
        The date and time the key version went, or will go, inactive, expressed in RFC 3339 timestamp format. This
        is when the key material will no longer be used to generate RRSIGs. For a key signing key (KSK) `DnssecKeyVersion`, this is
        populated after `PromoteZoneDnssecKeyVersion` has been called on its successor `DnssecKeyVersion`.

        **Example:** `2016-07-22T17:23:59:00Z`


        :return: The time_inactivated of this KskDnssecKeyVersion.
        :rtype: datetime
        """
        return self._time_inactivated

    @time_inactivated.setter
    def time_inactivated(self, time_inactivated):
        """
        Sets the time_inactivated of this KskDnssecKeyVersion.
        The date and time the key version went, or will go, inactive, expressed in RFC 3339 timestamp format. This
        is when the key material will no longer be used to generate RRSIGs. For a key signing key (KSK) `DnssecKeyVersion`, this is
        populated after `PromoteZoneDnssecKeyVersion` has been called on its successor `DnssecKeyVersion`.

        **Example:** `2016-07-22T17:23:59:00Z`


        :param time_inactivated: The time_inactivated of this KskDnssecKeyVersion.
        :type: datetime
        """
        self._time_inactivated = time_inactivated

    @property
    def time_unpublished(self):
        """
        Gets the time_unpublished of this KskDnssecKeyVersion.
        The date and time the key version was, or will be, unpublished, expressed in RFC 3339 timestamp format. This
        is when the corresponding DNSKEY will be removed from zone contents. For a key signing key (KSK) `DnssecKeyVersion`, this is
        populated after `PromoteZoneDnssecKeyVersion` has been called on its successor `DnssecKeyVersion`.

        **Example:** `2016-07-22T17:23:59:00Z`


        :return: The time_unpublished of this KskDnssecKeyVersion.
        :rtype: datetime
        """
        return self._time_unpublished

    @time_unpublished.setter
    def time_unpublished(self, time_unpublished):
        """
        Sets the time_unpublished of this KskDnssecKeyVersion.
        The date and time the key version was, or will be, unpublished, expressed in RFC 3339 timestamp format. This
        is when the corresponding DNSKEY will be removed from zone contents. For a key signing key (KSK) `DnssecKeyVersion`, this is
        populated after `PromoteZoneDnssecKeyVersion` has been called on its successor `DnssecKeyVersion`.

        **Example:** `2016-07-22T17:23:59:00Z`


        :param time_unpublished: The time_unpublished of this KskDnssecKeyVersion.
        :type: datetime
        """
        self._time_unpublished = time_unpublished

    @property
    def time_expired(self):
        """
        Gets the time_expired of this KskDnssecKeyVersion.
        The date and time at which the recommended key version publication/activation lifetime ends, expressed in RFC
        3339 timestamp format. This is when the corresponding DNSKEY should no longer exist in zone contents and no
        longer be used to generate RRSIGs. For a key sigining key (KSK), if `PromoteZoneDnssecKeyVersion` has not been called on this
        `DnssecKeyVersion`'s successor then it will remain active for arbitrarily long past its recommended lifetime.
        This prevents service disruption at the potential increased risk of key compromise.

        **Example:** `2016-07-22T17:23:59:00Z`


        :return: The time_expired of this KskDnssecKeyVersion.
        :rtype: datetime
        """
        return self._time_expired

    @time_expired.setter
    def time_expired(self, time_expired):
        """
        Sets the time_expired of this KskDnssecKeyVersion.
        The date and time at which the recommended key version publication/activation lifetime ends, expressed in RFC
        3339 timestamp format. This is when the corresponding DNSKEY should no longer exist in zone contents and no
        longer be used to generate RRSIGs. For a key sigining key (KSK), if `PromoteZoneDnssecKeyVersion` has not been called on this
        `DnssecKeyVersion`'s successor then it will remain active for arbitrarily long past its recommended lifetime.
        This prevents service disruption at the potential increased risk of key compromise.

        **Example:** `2016-07-22T17:23:59:00Z`


        :param time_expired: The time_expired of this KskDnssecKeyVersion.
        :type: datetime
        """
        self._time_expired = time_expired

    @property
    def time_promoted(self):
        """
        Gets the time_promoted of this KskDnssecKeyVersion.
        The date and time the key version was promoted expressed in RFC 3339 timestamp format.

        **Example:** `2016-07-22T17:23:59:00Z`


        :return: The time_promoted of this KskDnssecKeyVersion.
        :rtype: datetime
        """
        return self._time_promoted

    @time_promoted.setter
    def time_promoted(self, time_promoted):
        """
        Sets the time_promoted of this KskDnssecKeyVersion.
        The date and time the key version was promoted expressed in RFC 3339 timestamp format.

        **Example:** `2016-07-22T17:23:59:00Z`


        :param time_promoted: The time_promoted of this KskDnssecKeyVersion.
        :type: datetime
        """
        self._time_promoted = time_promoted

    @property
    def predecessor_dnssec_key_version_uuid(self):
        """
        Gets the predecessor_dnssec_key_version_uuid of this KskDnssecKeyVersion.
        When populated, this is the UUID of the `DnssecKeyVersion` that this `DnssecKeyVersion` will replace or has
        replaced.


        :return: The predecessor_dnssec_key_version_uuid of this KskDnssecKeyVersion.
        :rtype: str
        """
        return self._predecessor_dnssec_key_version_uuid

    @predecessor_dnssec_key_version_uuid.setter
    def predecessor_dnssec_key_version_uuid(self, predecessor_dnssec_key_version_uuid):
        """
        Sets the predecessor_dnssec_key_version_uuid of this KskDnssecKeyVersion.
        When populated, this is the UUID of the `DnssecKeyVersion` that this `DnssecKeyVersion` will replace or has
        replaced.


        :param predecessor_dnssec_key_version_uuid: The predecessor_dnssec_key_version_uuid of this KskDnssecKeyVersion.
        :type: str
        """
        self._predecessor_dnssec_key_version_uuid = predecessor_dnssec_key_version_uuid

    @property
    def successor_dnssec_key_version_uuid(self):
        """
        Gets the successor_dnssec_key_version_uuid of this KskDnssecKeyVersion.
        When populated, this is the UUID of the `DnssecKeyVersion` that will replace, or has replaced, this
        `DnssecKeyVersion`.


        :return: The successor_dnssec_key_version_uuid of this KskDnssecKeyVersion.
        :rtype: str
        """
        return self._successor_dnssec_key_version_uuid

    @successor_dnssec_key_version_uuid.setter
    def successor_dnssec_key_version_uuid(self, successor_dnssec_key_version_uuid):
        """
        Sets the successor_dnssec_key_version_uuid of this KskDnssecKeyVersion.
        When populated, this is the UUID of the `DnssecKeyVersion` that will replace, or has replaced, this
        `DnssecKeyVersion`.


        :param successor_dnssec_key_version_uuid: The successor_dnssec_key_version_uuid of this KskDnssecKeyVersion.
        :type: str
        """
        self._successor_dnssec_key_version_uuid = successor_dnssec_key_version_uuid

    @property
    def key_tag(self):
        """
        Gets the key_tag of this KskDnssecKeyVersion.
        The key tag associated with the `DnssecKeyVersion`. This key tag will be present in the RRSIG and DS records
        associated with the key material for this `DnssecKeyVersion`. For more information about key tags, see
        `RFC 4034`__.

        __ https://tools.ietf.org/html/rfc4034


        :return: The key_tag of this KskDnssecKeyVersion.
        :rtype: int
        """
        return self._key_tag

    @key_tag.setter
    def key_tag(self, key_tag):
        """
        Sets the key_tag of this KskDnssecKeyVersion.
        The key tag associated with the `DnssecKeyVersion`. This key tag will be present in the RRSIG and DS records
        associated with the key material for this `DnssecKeyVersion`. For more information about key tags, see
        `RFC 4034`__.

        __ https://tools.ietf.org/html/rfc4034


        :param key_tag: The key_tag of this KskDnssecKeyVersion.
        :type: int
        """
        self._key_tag = key_tag

    @property
    def ds_data(self):
        """
        Gets the ds_data of this KskDnssecKeyVersion.
        An array of data for DS records corresponding with this key version. An entry will exist for each
        supported DS digest algorithm.


        :return: The ds_data of this KskDnssecKeyVersion.
        :rtype: list[oci.dns.models.DnssecKeyVersionDsData]
        """
        return self._ds_data

    @ds_data.setter
    def ds_data(self, ds_data):
        """
        Sets the ds_data of this KskDnssecKeyVersion.
        An array of data for DS records corresponding with this key version. An entry will exist for each
        supported DS digest algorithm.


        :param ds_data: The ds_data of this KskDnssecKeyVersion.
        :type: list[oci.dns.models.DnssecKeyVersionDsData]
        """
        self._ds_data = ds_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
