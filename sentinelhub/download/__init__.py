"""
A download part of the package
"""

from .request import DownloadRequest
from .client import DownloadClient, get_json, get_xml
from .sentinelhub_client import SentinelHubDownloadClient
from .aws_client import AwsDownloadClient
