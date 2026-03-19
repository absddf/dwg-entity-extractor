"""
DWG Entity Extractor - Main module
"""

__version__ = "0.1.0"
__author__ = "absddf"

from dwg_extractor.parser import DWGParser
from dwg_extractor.entities.base import BaseEntity

__all__ = ["DWGParser", "BaseEntity"]
