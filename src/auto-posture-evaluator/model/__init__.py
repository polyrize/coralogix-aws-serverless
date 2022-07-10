# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: com/coralogix/xdr/ingestion/v1/audit_log.proto, com/coralogix/xdr/ingestion/v1/security_report.proto, com/coralogix/xdr/ingestion/v1/security_report_ingestion_service.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


class SecurityReportTestResultResult(betterproto.Enum):
    TEST_PASSED = 0
    TEST_FAILED = 1


@dataclass(eq=False, repr=False)
class AuditLogDescription(betterproto.Message):
    description: Optional[str] = betterproto.string_field(
        1, optional=True, group="_description"
    )


@dataclass(eq=False, repr=False)
class SecurityReport(betterproto.Message):
    context: "SecurityReportContext" = betterproto.message_field(1)
    test_results: List["SecurityReportTestResult"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class SecurityReportContext(betterproto.Message):
    application_name: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )
    subsystem_name: Optional[str] = betterproto.message_field(
        3, wraps=betterproto.TYPE_STRING
    )
    computer_name: Optional[str] = betterproto.message_field(
        4, wraps=betterproto.TYPE_STRING
    )
    provider: Optional[str] = betterproto.message_field(
        5, wraps=betterproto.TYPE_STRING
    )
    service: Optional[str] = betterproto.message_field(6, wraps=betterproto.TYPE_STRING)
    execution_id: Optional[str] = betterproto.message_field(
        7, wraps=betterproto.TYPE_STRING
    )


@dataclass(eq=False, repr=False)
class SecurityReportTestResult(betterproto.Message):
    name: Optional[str] = betterproto.message_field(3, wraps=betterproto.TYPE_STRING)
    start_time: datetime = betterproto.message_field(4)
    end_time: datetime = betterproto.message_field(5)
    item: Optional[str] = betterproto.message_field(6, wraps=betterproto.TYPE_STRING)
    item_type: Optional[str] = betterproto.message_field(
        7, wraps=betterproto.TYPE_STRING
    )
    result: "SecurityReportTestResultResult" = betterproto.enum_field(8)
    additional_data: Optional[
        "betterproto_lib_google_protobuf.Struct"
    ] = betterproto.message_field(9, optional=True, group="_additional_data")


@dataclass(eq=False, repr=False)
class PostSecurityReportRequest(betterproto.Message):
    security_report: "SecurityReport" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class PostSecurityReportResponse(betterproto.Message):
    pass


class SecurityReportIngestionServiceStub(betterproto.ServiceStub):
    async def post_security_report(
        self, *, api_key: str, security_report: "SecurityReport" = None
    ) -> "PostSecurityReportResponse":

        request = PostSecurityReportRequest()
        if security_report is not None:
            request.security_report = security_report

        return await self._unary_unary(
            "/com.coralogix.xdr.ingestion.v1.SecurityReportIngestionService/PostSecurityReport",
            request,
            PostSecurityReportResponse,
            metadata=[('authorization', api_key)]
        )

import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf