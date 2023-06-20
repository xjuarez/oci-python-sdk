# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry, circuit_breaker  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel, get_signer_from_authentication_type, AUTHENTICATION_TYPE_FIELD_NAME
from .models import oda_type_mapping
missing = Sentinel("Missing")


class OdapackageClient(object):
    """
    API to create and maintain Oracle Digital Assistant service instances.
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default values are connection timeout 10 seconds and read timeout 60 seconds. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.cloud.oracle.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
            by passing an instance of :py:class:`~oci.auth.signers.InstancePrincipalsSecurityTokenSigner` as the value for this keyword argument
        :type signer: :py:class:`~oci.signer.AbstractBaseSigner`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to all calls made by this service client (i.e. at the client level). There is no retry strategy applied by default.
            Retry strategies can also be applied at the operation level by passing a ``retry_strategy`` keyword argument as part of calling the operation.
            Any value provided at the operation level will override whatever is specified at the client level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

        :param obj circuit_breaker_strategy: (optional)
            A circuit breaker strategy to apply to all calls made by this service client (i.e. at the client level).
            This client uses :py:data:`~oci.circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY` as default if no circuit breaker strategy is provided.
            The specifics of circuit breaker strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/circuit_breakers.html>`__.

        :param function circuit_breaker_callback: (optional)
            Callback function to receive any exceptions triggerred by the circuit breaker.

        :param bool client_level_realm_specific_endpoint_template_enabled: (optional)
            A boolean flag to indicate whether or not this client should be created with realm specific endpoint template enabled or disable. By default, this will be set as None.

        :param allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this client should allow control characters in the response object. By default, the client will not
            allow control characters to be in the response object.
        """
        validate_config(config, signer=kwargs.get('signer'))
        if 'signer' in kwargs:
            signer = kwargs['signer']

        elif AUTHENTICATION_TYPE_FIELD_NAME in config:
            signer = get_signer_from_authentication_type(config)

        else:
            signer = Signer(
                tenancy=config["tenancy"],
                user=config["user"],
                fingerprint=config["fingerprint"],
                private_key_file_location=config.get("key_file"),
                pass_phrase=get_config_value_or_default(config, "pass_phrase"),
                private_key_content=config.get("key_content")
            )

        base_client_init_kwargs = {
            'regional_client': True,
            'service_endpoint': kwargs.get('service_endpoint'),
            'base_path': '/20190506',
            'service_endpoint_template': 'https://digitalassistant-api.{region}.oci.{secondLevelDomain}',
            'service_endpoint_template_per_realm': {  },  # noqa: E201 E202
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY),
            'client_level_realm_specific_endpoint_template_enabled': kwargs.get('client_level_realm_specific_endpoint_template_enabled')
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("odapackage", config, signer, oda_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def create_imported_package(self, create_imported_package_details, oda_instance_id, **kwargs):
        """
        Starts an asynchronous job to import a package into a Digital Assistant instance.

        To monitor the status of the job, take the `opc-work-request-id` response
        header value and use it to call `GET /workRequests/{workRequestId}`.


        :param oci.oda.models.CreateImportedPackageDetails create_imported_package_details: (required)
            Parameter values required to import the package.

        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.ImportedPackage`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/create_imported_package.py.html>`__ to see an example of how to use create_imported_package API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/importedPackages"
        method = "POST"
        operation_name = "create_imported_package"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_imported_package got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_imported_package_details,
                response_type="ImportedPackage",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_imported_package_details,
                response_type="ImportedPackage",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def delete_imported_package(self, oda_instance_id, package_id, **kwargs):
        """
        Starts an asynchronous job to delete a package from a Digital Assistant instance.

        To monitor the status of the job, take the `opc-work-request-id` response
        header value and use it to call `GET /workRequests/{workRequestId}`.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str package_id: (required)
            Unique Digital Assistant package identifier.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/delete_imported_package.py.html>`__ to see an example of how to use delete_imported_package API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'packageId']
        resource_path = "/odaInstances/{odaInstanceId}/importedPackages/{packageId}"
        method = "DELETE"
        operation_name = "delete_imported_package"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/ImportedPackage/DeleteImportedPackage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_imported_package got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "packageId": package_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_imported_package(self, oda_instance_id, package_id, **kwargs):
        """
        Returns a list of summaries for imported packages in the instance.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str package_id: (required)
            Unique Digital Assistant package identifier.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.ImportedPackage`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/get_imported_package.py.html>`__ to see an example of how to use get_imported_package API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'packageId']
        resource_path = "/odaInstances/{odaInstanceId}/importedPackages/{packageId}"
        method = "GET"
        operation_name = "get_imported_package"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/ImportedPackage/GetImportedPackage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_imported_package got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "packageId": package_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ImportedPackage",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ImportedPackage",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_package(self, oda_instance_id, package_id, **kwargs):
        """
        Returns details about a package, and how to import it.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str package_id: (required)
            Unique Digital Assistant package identifier.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.Package`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/get_package.py.html>`__ to see an example of how to use get_package API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'packageId']
        resource_path = "/odaInstances/{odaInstanceId}/packages/{packageId}"
        method = "GET"
        operation_name = "get_package"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/Package/GetPackage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_package got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "packageId": package_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Package",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Package",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def list_imported_packages(self, oda_instance_id, **kwargs):
        """
        Returns a list of summaries for imported packages in the instance.


        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str name: (optional)
            List only the information for the package with this name. Package names are unique to a publisher and may not change.

            Example: `My Package`

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The page at which to start retrieving results.

            You get this value from the `opc-next-page` header in a previous list request.
            To retireve the first page, omit this query parameter.

            Example: `MToxMA==`

        :param str sort_order: (optional)
            Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`.

            The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.oda.models.ImportedPackageSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/list_imported_packages.py.html>`__ to see an example of how to use list_imported_packages API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId']
        resource_path = "/odaInstances/{odaInstanceId}/importedPackages"
        method = "GET"
        operation_name = "list_imported_packages"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/ImportedPackageSummary/ListImportedPackages"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "name",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_imported_packages got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "name": kwargs.get("name", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ImportedPackageSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ImportedPackageSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def list_packages(self, **kwargs):
        """
        Returns a page of summaries for packages that are available for import. The optional odaInstanceId query
        parameter can be used to filter packages that are available for import by a specific instance. If odaInstanceId
        query parameter is not provided, the returned list will
        include packages available within the region indicated by the request URL. The optional resourceType query
        param may be specified to filter packages that contain the indicated resource type. If no resourceType query
        param is given, packages containing all resource types will be returned. The optional name query parameter can
        be used to limit the list to packages whose name matches the given name. The optional displayName query
        parameter can be used to limit the list to packages whose displayName matches the given name. The optional
        isLatestVersionOnly query parameter can be used to limit the returned list to include only the latest version
        of any given package. If not specified, all versions of any otherwise matching package will be returned.

        If the `opc-next-page` header appears in the response, then
        there are more items to retrieve. To get the next page in the subsequent
        GET request, include the header's value as the `page` query parameter.


        :param str oda_instance_id: (optional)
            List only the information for this Digital Assistant instance.

        :param str resource_type: (optional)
            Resource type identifier. Used to limit query results to the items which are applicable to the given type.

        :param str compartment_id: (optional)
            List the packages that belong to this compartment.

        :param str name: (optional)
            List only the information for the package with this name. Package names are unique to a publisher and may not change.

            Example: `My Package`

        :param str display_name: (optional)
            List only the information for the Digital Assistant instance with this user-friendly name. These names don't have to be unique and may change.

            Example: `My new resource`

        :param bool is_latest_version_only: (optional)
            Should we return only the latest version of a package (instead of all versions)?

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The page at which to start retrieving results.

            You get this value from the `opc-next-page` header in a previous list request.
            To retireve the first page, omit this query parameter.

            Example: `MToxMA==`

        :param str sort_order: (optional)
            Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`.

            The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.oda.models.PackageSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/list_packages.py.html>`__ to see an example of how to use list_packages API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = []
        resource_path = "/packages"
        method = "GET"
        operation_name = "list_packages"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/digital-assistant/20190506/PackageSummary/ListPackages"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "oda_instance_id",
            "resource_type",
            "compartment_id",
            "name",
            "display_name",
            "is_latest_version_only",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_packages got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "odaInstanceId": kwargs.get("oda_instance_id", missing),
            "resourceType": kwargs.get("resource_type", missing),
            "compartmentId": kwargs.get("compartment_id", missing),
            "name": kwargs.get("name", missing),
            "displayName": kwargs.get("display_name", missing),
            "isLatestVersionOnly": kwargs.get("is_latest_version_only", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PackageSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PackageSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def update_imported_package(self, update_imported_package_details, oda_instance_id, package_id, **kwargs):
        """
        Starts an asynchronous job to update a package within a Digital Assistant instance.

        To monitor the status of the job, take the `opc-work-request-id` response
        header value and use it to call `GET /workRequests/{workRequestId}`.


        :param oci.oda.models.UpdateImportedPackageDetails update_imported_package_details: (required)
            Parameter values required to import the package, with updated values.

        :param str oda_instance_id: (required)
            Unique Digital Assistant instance identifier.

        :param str package_id: (required)
            Unique Digital Assistant package identifier.

        :param bool is_replace_skills: (optional)
            Should old skills be replaced by new skills if packageId differs from already imported package?

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that you can retry the request if there's
            a timeout or server error without the risk of executing that same action again.

            Retry tokens expire after 24 hours, but they can become invalid before then if there are
            conflicting operations. For example, if an instance was deleted and purged from the system,
            then the service might reject a retry of the original creation request.

        :param str if_match: (optional)
            For optimistic concurrency control in a PUT or DELETE call for
            a Digital Assistant instance, set the `if-match` query parameter
            to the value of the `ETAG` header from a previous GET or POST
            response for that instance. The service updates or deletes the
            instance only if the etag that you provide matches the instance's
            current etag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing. This value is included in the opc-request-id response header.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.oda.models.ImportedPackage`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/oda/update_imported_package.py.html>`__ to see an example of how to use update_imported_package API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['odaInstanceId', 'packageId']
        resource_path = "/odaInstances/{odaInstanceId}/importedPackages/{packageId}"
        method = "PUT"
        operation_name = "update_imported_package"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "is_replace_skills",
            "opc_retry_token",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_imported_package got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "odaInstanceId": oda_instance_id,
            "packageId": package_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "isReplaceSkills": kwargs.get("is_replace_skills", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_imported_package_details,
                response_type="ImportedPackage",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_imported_package_details,
                response_type="ImportedPackage",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
