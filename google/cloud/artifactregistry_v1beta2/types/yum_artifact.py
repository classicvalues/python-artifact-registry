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
import proto  # type: ignore

from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.devtools.artifactregistry.v1beta2",
    manifest={
        "YumArtifact",
        "ImportYumArtifactsGcsSource",
        "ImportYumArtifactsRequest",
        "ImportYumArtifactsErrorInfo",
        "ImportYumArtifactsResponse",
        "ImportYumArtifactsMetadata",
    },
)


class YumArtifact(proto.Message):
    r"""A detailed representation of a Yum artifact.

    Attributes:
        name (str):
            Output only. The Artifact Registry resource
            name of the artifact.
        package_name (str):
            Output only. The yum package name of the
            artifact.
        package_type (google.cloud.artifactregistry_v1beta2.types.YumArtifact.PackageType):
            Output only. An artifact is a binary or
            source package.
        architecture (str):
            Output only. Operating system architecture of
            the artifact.
    """

    class PackageType(proto.Enum):
        r"""Package type is either binary or source."""
        PACKAGE_TYPE_UNSPECIFIED = 0
        BINARY = 1
        SOURCE = 2

    name = proto.Field(proto.STRING, number=1,)
    package_name = proto.Field(proto.STRING, number=2,)
    package_type = proto.Field(proto.ENUM, number=3, enum=PackageType,)
    architecture = proto.Field(proto.STRING, number=4,)


class ImportYumArtifactsGcsSource(proto.Message):
    r"""Google Cloud Storage location where the artifacts currently
    reside.

    Attributes:
        uris (Sequence[str]):
            Cloud Storage paths URI (e.g., gs://my_bucket//my_object).
        use_wildcards (bool):
            Supports URI wildcards for matching multiple
            objects from a single URI.
    """

    uris = proto.RepeatedField(proto.STRING, number=1,)
    use_wildcards = proto.Field(proto.BOOL, number=2,)


class ImportYumArtifactsRequest(proto.Message):
    r"""The request to import new yum artifacts.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_source (google.cloud.artifactregistry_v1beta2.types.ImportYumArtifactsGcsSource):
            Google Cloud Storage location where input
            content is located.

            This field is a member of `oneof`_ ``source``.
        parent (str):
            The name of the parent resource where the
            artifacts will be imported.
    """

    gcs_source = proto.Field(
        proto.MESSAGE, number=2, oneof="source", message="ImportYumArtifactsGcsSource",
    )
    parent = proto.Field(proto.STRING, number=1,)


class ImportYumArtifactsErrorInfo(proto.Message):
    r"""Error information explaining why a package was not imported.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_source (google.cloud.artifactregistry_v1beta2.types.ImportYumArtifactsGcsSource):
            Google Cloud Storage location requested.

            This field is a member of `oneof`_ ``source``.
        error (google.rpc.status_pb2.Status):
            The detailed error status.
    """

    gcs_source = proto.Field(
        proto.MESSAGE, number=1, oneof="source", message="ImportYumArtifactsGcsSource",
    )
    error = proto.Field(proto.MESSAGE, number=2, message=status_pb2.Status,)


class ImportYumArtifactsResponse(proto.Message):
    r"""The response message from importing YUM artifacts.

    Attributes:
        yum_artifacts (Sequence[google.cloud.artifactregistry_v1beta2.types.YumArtifact]):
            The yum artifacts imported.
        errors (Sequence[google.cloud.artifactregistry_v1beta2.types.ImportYumArtifactsErrorInfo]):
            Detailed error info for artifacts that were
            not imported.
    """

    yum_artifacts = proto.RepeatedField(proto.MESSAGE, number=1, message="YumArtifact",)
    errors = proto.RepeatedField(
        proto.MESSAGE, number=2, message="ImportYumArtifactsErrorInfo",
    )


class ImportYumArtifactsMetadata(proto.Message):
    r"""The operation metadata for importing artifacts.
    """


__all__ = tuple(sorted(__protobuf__.manifest))
