# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Sequence,
    Tuple,
    Optional,
    Iterator,
)

from google.cloud.artifactregistry_v1beta2.types import file
from google.cloud.artifactregistry_v1beta2.types import package
from google.cloud.artifactregistry_v1beta2.types import repository
from google.cloud.artifactregistry_v1beta2.types import tag
from google.cloud.artifactregistry_v1beta2.types import version


class ListRepositoriesPager:
    """A pager for iterating through ``list_repositories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1beta2.types.ListRepositoriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``repositories`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRepositories`` requests and continue to iterate
    through the ``repositories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1beta2.types.ListRepositoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., repository.ListRepositoriesResponse],
        request: repository.ListRepositoriesRequest,
        response: repository.ListRepositoriesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1beta2.types.ListRepositoriesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1beta2.types.ListRepositoriesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = repository.ListRepositoriesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[repository.ListRepositoriesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[repository.Repository]:
        for page in self.pages:
            yield from page.repositories

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRepositoriesAsyncPager:
    """A pager for iterating through ``list_repositories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1beta2.types.ListRepositoriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``repositories`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRepositories`` requests and continue to iterate
    through the ``repositories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1beta2.types.ListRepositoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[repository.ListRepositoriesResponse]],
        request: repository.ListRepositoriesRequest,
        response: repository.ListRepositoriesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1beta2.types.ListRepositoriesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1beta2.types.ListRepositoriesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = repository.ListRepositoriesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[repository.ListRepositoriesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[repository.Repository]:
        async def async_generator():
            async for page in self.pages:
                for response in page.repositories:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPackagesPager:
    """A pager for iterating through ``list_packages`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1beta2.types.ListPackagesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``packages`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPackages`` requests and continue to iterate
    through the ``packages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1beta2.types.ListPackagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., package.ListPackagesResponse],
        request: package.ListPackagesRequest,
        response: package.ListPackagesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1beta2.types.ListPackagesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1beta2.types.ListPackagesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = package.ListPackagesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[package.ListPackagesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[package.Package]:
        for page in self.pages:
            yield from page.packages

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPackagesAsyncPager:
    """A pager for iterating through ``list_packages`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1beta2.types.ListPackagesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``packages`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPackages`` requests and continue to iterate
    through the ``packages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1beta2.types.ListPackagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[package.ListPackagesResponse]],
        request: package.ListPackagesRequest,
        response: package.ListPackagesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1beta2.types.ListPackagesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1beta2.types.ListPackagesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = package.ListPackagesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[package.ListPackagesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[package.Package]:
        async def async_generator():
            async for page in self.pages:
                for response in page.packages:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVersionsPager:
    """A pager for iterating through ``list_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1beta2.types.ListVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVersions`` requests and continue to iterate
    through the ``versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1beta2.types.ListVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., version.ListVersionsResponse],
        request: version.ListVersionsRequest,
        response: version.ListVersionsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1beta2.types.ListVersionsRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1beta2.types.ListVersionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = version.ListVersionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[version.ListVersionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[version.Version]:
        for page in self.pages:
            yield from page.versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVersionsAsyncPager:
    """A pager for iterating through ``list_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1beta2.types.ListVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVersions`` requests and continue to iterate
    through the ``versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1beta2.types.ListVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[version.ListVersionsResponse]],
        request: version.ListVersionsRequest,
        response: version.ListVersionsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1beta2.types.ListVersionsRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1beta2.types.ListVersionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = version.ListVersionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[version.ListVersionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[version.Version]:
        async def async_generator():
            async for page in self.pages:
                for response in page.versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFilesPager:
    """A pager for iterating through ``list_files`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1beta2.types.ListFilesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``files`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFiles`` requests and continue to iterate
    through the ``files`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1beta2.types.ListFilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., file.ListFilesResponse],
        request: file.ListFilesRequest,
        response: file.ListFilesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1beta2.types.ListFilesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1beta2.types.ListFilesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = file.ListFilesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[file.ListFilesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[file.File]:
        for page in self.pages:
            yield from page.files

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFilesAsyncPager:
    """A pager for iterating through ``list_files`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1beta2.types.ListFilesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``files`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFiles`` requests and continue to iterate
    through the ``files`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1beta2.types.ListFilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[file.ListFilesResponse]],
        request: file.ListFilesRequest,
        response: file.ListFilesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1beta2.types.ListFilesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1beta2.types.ListFilesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = file.ListFilesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[file.ListFilesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[file.File]:
        async def async_generator():
            async for page in self.pages:
                for response in page.files:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTagsPager:
    """A pager for iterating through ``list_tags`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1beta2.types.ListTagsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``tags`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTags`` requests and continue to iterate
    through the ``tags`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1beta2.types.ListTagsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., tag.ListTagsResponse],
        request: tag.ListTagsRequest,
        response: tag.ListTagsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1beta2.types.ListTagsRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1beta2.types.ListTagsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = tag.ListTagsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[tag.ListTagsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[tag.Tag]:
        for page in self.pages:
            yield from page.tags

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTagsAsyncPager:
    """A pager for iterating through ``list_tags`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1beta2.types.ListTagsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``tags`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTags`` requests and continue to iterate
    through the ``tags`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1beta2.types.ListTagsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[tag.ListTagsResponse]],
        request: tag.ListTagsRequest,
        response: tag.ListTagsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1beta2.types.ListTagsRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1beta2.types.ListTagsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = tag.ListTagsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[tag.ListTagsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[tag.Tag]:
        async def async_generator():
            async for page in self.pages:
                for response in page.tags:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
