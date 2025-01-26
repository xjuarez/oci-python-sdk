# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TopProcessesUsage(object):
    """
    Aggregated data for top processes on a specific date.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TopProcessesUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param command:
            The value to assign to the command property of this TopProcessesUsage.
        :type command: str

        :param container_id:
            The value to assign to the container_id property of this TopProcessesUsage.
        :type container_id: str

        :param process_hash:
            The value to assign to the process_hash property of this TopProcessesUsage.
        :type process_hash: str

        :param cpu_usage:
            The value to assign to the cpu_usage property of this TopProcessesUsage.
        :type cpu_usage: float

        :param cpu_utilization:
            The value to assign to the cpu_utilization property of this TopProcessesUsage.
        :type cpu_utilization: float

        :param memory_utilization:
            The value to assign to the memory_utilization property of this TopProcessesUsage.
        :type memory_utilization: float

        :param virtual_memory_in_mbs:
            The value to assign to the virtual_memory_in_mbs property of this TopProcessesUsage.
        :type virtual_memory_in_mbs: float

        :param physical_memory_in_mbs:
            The value to assign to the physical_memory_in_mbs property of this TopProcessesUsage.
        :type physical_memory_in_mbs: float

        :param max_process_count:
            The value to assign to the max_process_count property of this TopProcessesUsage.
        :type max_process_count: int

        """
        self.swagger_types = {
            'command': 'str',
            'container_id': 'str',
            'process_hash': 'str',
            'cpu_usage': 'float',
            'cpu_utilization': 'float',
            'memory_utilization': 'float',
            'virtual_memory_in_mbs': 'float',
            'physical_memory_in_mbs': 'float',
            'max_process_count': 'int'
        }

        self.attribute_map = {
            'command': 'command',
            'container_id': 'containerId',
            'process_hash': 'processHash',
            'cpu_usage': 'cpuUsage',
            'cpu_utilization': 'cpuUtilization',
            'memory_utilization': 'memoryUtilization',
            'virtual_memory_in_mbs': 'virtualMemoryInMBs',
            'physical_memory_in_mbs': 'physicalMemoryInMBs',
            'max_process_count': 'maxProcessCount'
        }

        self._command = None
        self._container_id = None
        self._process_hash = None
        self._cpu_usage = None
        self._cpu_utilization = None
        self._memory_utilization = None
        self._virtual_memory_in_mbs = None
        self._physical_memory_in_mbs = None
        self._max_process_count = None

    @property
    def command(self):
        """
        **[Required]** Gets the command of this TopProcessesUsage.
        Command line and arguments used to launch process.


        :return: The command of this TopProcessesUsage.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this TopProcessesUsage.
        Command line and arguments used to launch process.


        :param command: The command of this TopProcessesUsage.
        :type: str
        """
        self._command = command

    @property
    def container_id(self):
        """
        Gets the container_id of this TopProcessesUsage.
        Container id if this process corresponds to a running container in the host.


        :return: The container_id of this TopProcessesUsage.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """
        Sets the container_id of this TopProcessesUsage.
        Container id if this process corresponds to a running container in the host.


        :param container_id: The container_id of this TopProcessesUsage.
        :type: str
        """
        self._container_id = container_id

    @property
    def process_hash(self):
        """
        **[Required]** Gets the process_hash of this TopProcessesUsage.
        Unique identifier for a process.


        :return: The process_hash of this TopProcessesUsage.
        :rtype: str
        """
        return self._process_hash

    @process_hash.setter
    def process_hash(self, process_hash):
        """
        Sets the process_hash of this TopProcessesUsage.
        Unique identifier for a process.


        :param process_hash: The process_hash of this TopProcessesUsage.
        :type: str
        """
        self._process_hash = process_hash

    @property
    def cpu_usage(self):
        """
        **[Required]** Gets the cpu_usage of this TopProcessesUsage.
        Process CPU usage.


        :return: The cpu_usage of this TopProcessesUsage.
        :rtype: float
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        """
        Sets the cpu_usage of this TopProcessesUsage.
        Process CPU usage.


        :param cpu_usage: The cpu_usage of this TopProcessesUsage.
        :type: float
        """
        self._cpu_usage = cpu_usage

    @property
    def cpu_utilization(self):
        """
        **[Required]** Gets the cpu_utilization of this TopProcessesUsage.
        Process CPU utilization percentage.


        :return: The cpu_utilization of this TopProcessesUsage.
        :rtype: float
        """
        return self._cpu_utilization

    @cpu_utilization.setter
    def cpu_utilization(self, cpu_utilization):
        """
        Sets the cpu_utilization of this TopProcessesUsage.
        Process CPU utilization percentage.


        :param cpu_utilization: The cpu_utilization of this TopProcessesUsage.
        :type: float
        """
        self._cpu_utilization = cpu_utilization

    @property
    def memory_utilization(self):
        """
        **[Required]** Gets the memory_utilization of this TopProcessesUsage.
        Process memory utilization percentage.


        :return: The memory_utilization of this TopProcessesUsage.
        :rtype: float
        """
        return self._memory_utilization

    @memory_utilization.setter
    def memory_utilization(self, memory_utilization):
        """
        Sets the memory_utilization of this TopProcessesUsage.
        Process memory utilization percentage.


        :param memory_utilization: The memory_utilization of this TopProcessesUsage.
        :type: float
        """
        self._memory_utilization = memory_utilization

    @property
    def virtual_memory_in_mbs(self):
        """
        **[Required]** Gets the virtual_memory_in_mbs of this TopProcessesUsage.
        Process virtual memory in Megabytes.


        :return: The virtual_memory_in_mbs of this TopProcessesUsage.
        :rtype: float
        """
        return self._virtual_memory_in_mbs

    @virtual_memory_in_mbs.setter
    def virtual_memory_in_mbs(self, virtual_memory_in_mbs):
        """
        Sets the virtual_memory_in_mbs of this TopProcessesUsage.
        Process virtual memory in Megabytes.


        :param virtual_memory_in_mbs: The virtual_memory_in_mbs of this TopProcessesUsage.
        :type: float
        """
        self._virtual_memory_in_mbs = virtual_memory_in_mbs

    @property
    def physical_memory_in_mbs(self):
        """
        **[Required]** Gets the physical_memory_in_mbs of this TopProcessesUsage.
        Procress physical memory in Megabytes.


        :return: The physical_memory_in_mbs of this TopProcessesUsage.
        :rtype: float
        """
        return self._physical_memory_in_mbs

    @physical_memory_in_mbs.setter
    def physical_memory_in_mbs(self, physical_memory_in_mbs):
        """
        Sets the physical_memory_in_mbs of this TopProcessesUsage.
        Procress physical memory in Megabytes.


        :param physical_memory_in_mbs: The physical_memory_in_mbs of this TopProcessesUsage.
        :type: float
        """
        self._physical_memory_in_mbs = physical_memory_in_mbs

    @property
    def max_process_count(self):
        """
        **[Required]** Gets the max_process_count of this TopProcessesUsage.
        Maximum number of processes running at time of collection.


        :return: The max_process_count of this TopProcessesUsage.
        :rtype: int
        """
        return self._max_process_count

    @max_process_count.setter
    def max_process_count(self, max_process_count):
        """
        Sets the max_process_count of this TopProcessesUsage.
        Maximum number of processes running at time of collection.


        :param max_process_count: The max_process_count of this TopProcessesUsage.
        :type: int
        """
        self._max_process_count = max_process_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
