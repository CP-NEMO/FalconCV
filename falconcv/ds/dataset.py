import abc
from abc import ABCMeta
from pathlib import Path
import dask
from dask import delayed
from dask.diagnostics import ProgressBar
import logging

logger = logging.getLogger(__name__)
from falconcv.util import LibUtil, FileUtil

DEP_KEY = "DEPENDENCIES"


class DatasetDownloader(metaclass=ABCMeta):
    def __init__(self):
        self._dependencies = {}
        self._images = []
        self._task = None
        self._split = None
        self._labels_map = {}
        self._slabels_map = {}
        self._remote_dep = {}

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, value):
        self._task = value

    @property
    def split(self):
        return self._split

    @split.setter
    def split(self, value):
        self._split = value

    @property
    def labels_map(self):
        return self._labels_map

    @labels_map.setter
    def labels_map(self, value):
        self._labels_map = value

    @property
    def slabels_map(self):
        return self._slabels_map

    @slabels_map.setter
    def slabels_map(self, value):
        self._slabels_map = value

    def _home(self) -> Path:
        """ @:return the current dataset path """
        ds_home = LibUtil.datasets_home()
        ds_name = type(self).__name__
        ds_path = ds_home.joinpath(ds_name)
        ds_path.mkdir(exist_ok=True)
        return ds_path

    def _download_dependencies(self):
        """Download the dataset dependencies"""
        # delayed_tasks = {}
        # for dep_name, dep_uri in self._remote_dep.items():
        #     task = delayed(FileUtil.download_file)(dep_uri, self._home())
        #     delayed_tasks[dep_name] = task
        # with ProgressBar():
        #     self._dependencies = dask.compute(delayed_tasks)[0]
        logger.info("Downloading {} dataset dependencies, it can take a few minutes".format(type(self).__name__))
        for dep_name, dep_uri in self._remote_dep.items():
            self._dependencies[dep_name] = FileUtil.download_file(dep_uri, self._home(), show_progress=True, unzip=True)
        logger.info("Download dependencies done")

    def _get_dependency(self, name):
        """@:return: "a dependency path """
        return str(self._dependencies.get(name, None))

    @abc.abstractmethod
    def fetch(self, n=None, labels=None, batch_size: int = 200):
        raise NotImplementedError

    @abc.abstractmethod
    def setup(self, split=None, task=None):
        self._split = split
        self._task = task
        self._download_dependencies()  # download the dataset files dependencies
