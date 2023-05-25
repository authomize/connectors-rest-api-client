# generated by datamodel-codegen:
#   filename:  openapi.json
#   timestamp: 2023-05-25T08:44:02+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Extra, Field, constr


class AccessByType(Enum):
    account = 'account'
    grouping = 'grouping'


class AccessToType(Enum):
    asset = 'asset'
    grouping = 'grouping'


class AddIncidentCommentRequestSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    content: constr(max_length=1025) = Field(
        ..., description='Content of comment.', title='Content'
    )


class AicpaTsc2017Standard(Enum):
    CC1_1 = 'CC1.1'
    CC6_3 = 'CC6.3'
    CC5_1 = 'CC5.1'
    CC5_3 = 'CC5.3'
    CC6_1 = 'CC6.1'
    CC6_2 = 'CC6.2'
    CC6_7 = 'CC6.7'
    CC6_6 = 'CC6.6'
    CC3_2 = 'CC3.2'
    CC3_3 = 'CC3.3'
    CC3_4 = 'CC3.4'


class AlertCategoryType(Enum):
    Change_Management = 'Change Management'
    Misconfiguration = 'Misconfiguration'
    Exposure = 'Exposure'
    Privileged_Access = 'Privileged Access'
    Suspicious_Behavior = 'Suspicious Behavior'
    Least_Privilege = 'Least Privilege'
    Custom = 'Custom'
    IAM_Infrastructure_Security = 'IAM Infrastructure Security'
    Account_Takeover_Protection = 'Account Takeover Protection'
    Stale_Access = 'Stale Access'
    Initial_Access = 'Initial Access'
    Over_privileges = 'Over-privileges'
    Privilege_Escalation = 'Privilege Escalation'
    Lateral_Movement = 'Lateral Movement'
    Detection = 'Detection'
    Persistence = 'Persistence'
    Evasion = 'Evasion'
    Account_Takeover = 'Account Takeover'
    Account_Impersonation__PE__LM_ = 'Account Impersonation (PE, LM)'


class AppIdFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_eq: Optional[str] = Field(
        default=None, alias='$eq', description='Equals To', title='$Eq'
    )


class AssetExpansion(Enum):
    sourceApp = 'sourceApp'
    tags = 'tags'


class AssetIdFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_in: Optional[List[str]] = Field(
        default=[], alias='$in', description='In', title='$In'
    )


class AttackTacticType(Enum):
    Collection = 'Collection'
    Credential_Access = 'Credential Access'
    Defense_Evasion = 'Defense Evasion'
    Discovery = 'Discovery'
    Exfiltration = 'Exfiltration'
    Impact = 'Impact'
    Initial_Access = 'Initial Access'
    Lateral_Movement = 'Lateral Movement'
    Persistence = 'Persistence'
    Privilege_Escalation = 'Privilege Escalation'


class CampaignExpansion(Enum):
    owner = 'owner'


class CampaignStatus(Enum):
    draft = 'draft'
    initializing = 'initializing'
    running = 'running'
    completed = 'completed'
    failed = 'failed'
    empty = 'empty'
    overdue = 'overdue'


class CampaignStatusFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_in: Optional[List[CampaignStatus]] = Field(
        default=[], alias='$in', description='In'
    )


class Ccm301Standard(Enum):
    AIS_04 = 'AIS-04'
    IAM_01 = 'IAM-01'
    IAM_02 = 'IAM-02'
    IAM_03 = 'IAM-03'
    IAM_04 = 'IAM-04'
    IAM_05 = 'IAM-05'
    IAM_06 = 'IAM-06'
    IAM_07 = 'IAM-07'
    IAM_08 = 'IAM-08'
    IAM_09 = 'IAM-09'
    IAM_10 = 'IAM-10'
    IAM_11 = 'IAM-11'
    IAM_12 = 'IAM-12'
    IAM_13 = 'IAM-13'
    GRM_06 = 'GRM-06'
    IVS_06 = 'IVS-06'
    IVS_08 = 'IVS-08'
    DSI_04 = 'DSI-04'


class Ccm402Standard(Enum):
    IAM_01 = 'IAM-01'
    IAM_02 = 'IAM-02'
    IAM_03 = 'IAM-03'
    IAM_04 = 'IAM-04'
    IAM_05 = 'IAM-05'
    IAM_06 = 'IAM-06'
    IAM_07 = 'IAM-07'
    IAM_08 = 'IAM-08'
    IAM_09 = 'IAM-09'
    IAM_10 = 'IAM-10'
    IAM_11 = 'IAM-11'
    IAM_12 = 'IAM-12'
    IAM_13 = 'IAM-13'
    IAM_14 = 'IAM-14'
    IAM_15 = 'IAM-15'
    IAM_16 = 'IAM-16'
    IVS_03 = 'IVS-03'
    IVS_04 = 'IVS-04'
    DSP_07 = 'DSP-07'
    DSP_08 = 'DSP-08'
    DSP_10 = 'DSP-10'
    AIS_03 = 'AIS-03'
    DSP_17 = 'DSP-17'
    DSP_01 = 'DSP-01'
    HRS_05 = 'HRS-05'


class CisV8Standard(Enum):
    field_3_1 = '3.1'
    field_3_3 = '3.3'
    field_6_8 = '6.8'
    field_5_4 = '5.4'
    field_12_7 = '12.7'
    field_6_5 = '6.5'
    field_6_2 = '6.2'
    field_5_3 = '5.3'
    field_12_2 = '12.2'
    field_6_1 = '6.1'
    field_5_1 = '5.1'
    field_4_11 = '4.11'
    field_13_4 = '13.4'
    field_13_9 = '13.9'
    field_13_10 = '13.10'


class Cisv8(BaseModel):
    values: List[CisV8Standard] = Field(..., description='Values')
    id: Optional[str] = Field(default='cisv8', description='UniqueID', title='Id')
    name: Optional[str] = Field(default='CIS v.8', description='Name', title='Name')


class CommentSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    id: str = Field(..., description='Unique ID of comment.', title='Id')
    content: constr(max_length=1025) = Field(
        ..., description='Content of comment.', title='Content'
    )


class EmailFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_in: Optional[List[str]] = Field(
        default=[], alias='$in', description='In', title='$In'
    )


class EventStatusType(Enum):
    Open = 'Open'
    InProgress = 'InProgress'
    WaitingForInput = 'WaitingForInput'
    Closed = 'Closed'


class FieldName(Enum):
    name = 'name'
    status = 'status'
    startDate = 'startDate'
    endDate = 'endDate'
    createdAt = 'createdAt'
    reviewerType = 'reviewerType'
    templateName = 'templateName'


class IdFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_in: Optional[List[str]] = Field(
        default=[], alias='$in', description='In', title='$In'
    )


class IdentityExpansion(Enum):
    account = 'account'
    tags = 'tags'


class IncidentExpansion(Enum):
    policy = 'policy'
    assignee = 'assignee'


class IncidentsCreatedAtFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_lte: Optional[datetime] = Field(
        default=None, alias='$lte', description='Less Than Or Equals To', title='$Lte'
    )
    field_gte: Optional[datetime] = Field(
        default=None,
        alias='$gte',
        description='Greater Than Or Equals To',
        title='$Gte',
    )
    field_lt: Optional[datetime] = Field(
        default=None, alias='$lt', description='Less Than', title='$Lt'
    )
    field_gt: Optional[datetime] = Field(
        default=None, alias='$gt', description='Greater Than', title='$Gt'
    )


class IncidentsIsResolvedFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_eq: Optional[bool] = Field(
        default=None, alias='$eq', description='Equals To', title='$Eq'
    )


class IncidentsPolicyIdFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_eq: Optional[str] = Field(
        default=None, alias='$eq', description='Equals To', title='$Eq'
    )


class IncidentsPolicyTempalteIdFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_eq: Optional[str] = Field(
        default=None, alias='$eq', description='Equals To', title='$Eq'
    )


class IncidentsStatusFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_in: Optional[List[EventStatusType]] = Field(
        default=[], alias='$in', description='In'
    )


class IncidentsUpdatedAtFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_lte: Optional[datetime] = Field(
        default=None, alias='$lte', description='Less Than Or Equals To', title='$Lte'
    )
    field_gte: Optional[datetime] = Field(
        default=None,
        alias='$gte',
        description='Greater Than Or Equals To',
        title='$Gte',
    )
    field_lt: Optional[datetime] = Field(
        default=None, alias='$lt', description='Less Than', title='$Lt'
    )
    field_gt: Optional[datetime] = Field(
        default=None, alias='$gt', description='Greater Than', title='$Gt'
    )


class InventoryObjects(Enum):
    identity = 'identity'
    account = 'account'
    asset = 'asset'
    privilege = 'privilege'
    other = 'other'


class IsAliveResponse(BaseModel):
    isAlive: bool = Field(..., description='**isAlive**', title='Isalive')


class IsoIec27001Standard(Enum):
    A_6_1_2 = 'A.6.1.2'
    A_8_1_1 = 'A.8.1.1'
    A_8_1_3 = 'A.8.1.3'
    A_8_3_3 = 'A.8.3.3'
    A_9_1_1 = 'A.9.1.1'
    A_9_2_1 = 'A.9.2.1'
    A_9_2_3 = 'A.9.2.3'
    A_9_2_6 = 'A.9.2.6'
    A_9_4_1 = 'A.9.4.1'
    A_9_1_2 = 'A.9.1.2'
    A_9_4_2 = 'A.9.4.2'
    A_9_2_2 = 'A.9.2.2'
    A_13_2_1 = 'A.13.2.1'
    A_9_4_3 = 'A.9.4.3'
    A_7_2_2 = 'A.7.2.2'
    A_9_4_5 = 'A.9.4.5'
    A_8_2_3 = 'A.8.2.3'
    A_7_3_1 = 'A.7.3.1'
    A_8_1_4 = 'A.8.1.4'


class MeResponse(BaseModel):
    version: Optional[str] = Field(
        default='4.1.2', description='**version**', title='Version'
    )
    id: str = Field(..., description='**id**', title='Id')
    tenant: str = Field(..., description='**tenant**', title='Tenant')


class NonPaginatedResponseSchemaCommentSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    data: CommentSchema = Field(..., description='Actual Data', title='Data')


class OriginIdFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_in: Optional[List[str]] = Field(
        default=[], alias='$in', description='In', title='$In'
    )


class PaginationRequestSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    limit: Optional[int] = Field(default=None, description='Limit', title='Limit')
    nextPage: Optional[str] = Field(
        default=None, description='Starting after', title='NextPage'
    )


class PaginationResponseSchema(BaseModel):
    limit: Optional[int] = Field(default=20, description='Limit', title='Limit')
    hasMore: Optional[bool] = Field(
        default=None, description='Has more? `true` or `false`.', title='HasMore'
    )
    nextPage: Optional[str] = Field(
        default=None, description='Starting after', title='NextPage'
    )


class PermissionsExpansion(Enum):
    reviewer_user = 'reviewer.user'


class PolicySchema(BaseModel):
    id: str = Field(..., description='Unique id of policy.', title='Id')
    name: str = Field(..., description='Name of policy.', title='Name')
    templateId: str = Field(..., description='Template ID', title='Templateid')


class ReviewStatus(Enum):
    pending = 'pending'
    completed = 'completed'
    reviewing = 'reviewing'
    notified = 'notified'
    inactive = 'inactive'


class ReviewerExpansion(Enum):
    user = 'user'


class SearchAssetsSortFields(Enum):
    asset_name = 'asset.name'


class SearchIdentitiesFilterBody(BaseModel):
    class Config:
        extra = Extra.forbid

    email: Optional[EmailFilter] = Field(
        default=None, description='Email.', title='Email'
    )
    authomizeId: Optional[IdFilter] = Field(
        default=None, description='Authomize ID for the Identity', title='Authomizeid'
    )


class SearchIdentitiesSortFields(Enum):
    identity_name = 'identity.name'


class SearchIncidentsSortFields(Enum):
    createdAt = 'createdAt'
    updatedAt = 'updatedAt'
    severity = 'severity'
    status = 'status'
    isResolved = 'isResolved'


class Selection(Enum):
    keep = 'keep'
    revoke = 'revoke'
    null = 'null'


class SeverityType(Enum):
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'
    Critical = 'Critical'


class SortOrder(Enum):
    ASC = 'ASC'
    DESC = 'DESC'


class SortSchemaFieldName(BaseModel):
    class Config:
        extra = Extra.forbid

    fieldName: FieldName = Field(
        ..., description='Sort By Field Name', title='FieldName'
    )
    order: Optional[SortOrder] = Field(
        default='ASC', description='Sort Order', title='Order'
    )


class SortSchemaSearchAssetsSortFields(BaseModel):
    class Config:
        extra = Extra.forbid

    fieldName: SearchAssetsSortFields = Field(
        ..., description='Sort By Field Name', title='FieldName'
    )
    order: Optional[SortOrder] = Field(
        default='ASC', description='Sort Order', title='Order'
    )


class SortSchemaSearchIdentitiesSortFields(BaseModel):
    class Config:
        extra = Extra.forbid

    fieldName: SearchIdentitiesSortFields = Field(
        ..., description='Sort By Field Name', title='FieldName'
    )
    order: Optional[SortOrder] = Field(
        default='ASC', description='Sort Order', title='Order'
    )


class SortSchemaSearchIncidentsSortFields(BaseModel):
    class Config:
        extra = Extra.forbid

    fieldName: SearchIncidentsSortFields = Field(
        ..., description='Sort By Field Name', title='FieldName'
    )
    order: Optional[SortOrder] = Field(
        default='ASC', description='Sort Order', title='Order'
    )


class SourceAppSchema(BaseModel):
    id: str = Field(..., description='Unique ID', title='Id')
    name: str = Field(..., description='Name', title='Name')


class TagSchema(BaseModel):
    id: str = Field(..., description='Authomize ID for the Tag', title='Id')
    name: str = Field(..., description='Name of the tag', title='Name')
    description: str = Field(
        ..., description='Description of the tag', title='Description'
    )


class UniqueIdFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_in: Optional[List[str]] = Field(
        default=[], alias='$in', description='In', title='$In'
    )


class UpdateIncidentRequestSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    assigneeId: Optional[str] = Field(
        default=None,
        description='ID of the entity assigned to this incident.',
        title='Assigneeid',
    )
    status: Optional[EventStatusType] = Field(
        default=None,
        description='The status of the incident (Open, InProgress, WaitingForInput, or Closed).',
    )
    severity: Optional[SeverityType] = Field(
        default=None,
        description='The severity of the incident (Low, Medium, High or Critical).',
    )


class UserSchema(BaseModel):
    userId: str = Field(..., description='Unique ID', title='Userid')
    userFirstName: str = Field(..., description='First Name', title='Userfirstname')
    userLastName: str = Field(..., description='Last Name', title='Userlastname')
    userEmail: str = Field(..., description='Email', title='Useremail')


class ValidationError(BaseModel):
    loc: List[str] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class AicpaTsc2017(BaseModel):
    values: List[AicpaTsc2017Standard] = Field(..., description='Values')
    id: Optional[str] = Field(
        default='aicpaTsc2017', description='UniqueID', title='Id'
    )
    name: Optional[str] = Field(
        default='SOC 2 (TSC 2017)', description='Name', title='Name'
    )


class AssetSchema(BaseModel):
    authomizeId: str = Field(..., description='Unique ID', title='Authomizeid')
    name: str = Field(..., description='Name', title='Name')
    type: str = Field(..., description='Type', title='Type')
    originType: Optional[str] = Field(
        default=None,
        description='The asset type in the source system. The default is the canonical type (if not mentioned).\n',
        title='Origintype',
    )
    sourceApp: Optional[SourceAppSchema] = Field(
        default=None, description='Source App', title='Sourceapp'
    )
    createdAt: Optional[datetime] = Field(
        default=None,
        description='The date (in ISO 8601 format) that the asset was created.\n',
        title='Createdat',
    )
    lastUsedAt: Optional[str] = Field(
        default=None,
        description='The date (in ISO 8601 format) of the last time that the asset was in use.',
        title='Lastusedat',
    )
    href: Optional[str] = Field(default=None, description='HREF', title='Href')
    uniqueId: Optional[str] = Field(
        default=None, description='The Unique Identifier.', title='Uniqueid'
    )
    originId: Optional[str] = Field(
        default=None,
        description='The identifier of the asset from the origin system.',
        title='Originid',
    )
    description: Optional[str] = Field(
        default=None, description='Asset description', title='Description'
    )
    tags: Optional[List[TagSchema]] = Field(
        default=None, description='Expanded Tags', title='Tags'
    )
    incidentsCount: Optional[int] = Field(
        default=None,
        description='Number of associated incidents',
        title='Incidentscount',
    )


class CampaignPermissionDecisionFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_in: Optional[List[Selection]] = Field(
        default=[], alias='$in', description='In'
    )


class CampaignPermissionsSearchFilterBody(BaseModel):
    class Config:
        extra = Extra.forbid

    decision: Optional[CampaignPermissionDecisionFilter] = Field(
        default=None,
        description='Reviewer decisions (keep, revoke or null).\n',
        title='Decision',
    )


class CampaignSchema(BaseModel):
    id: str = Field(..., description='Unique ID of campaign', title='Id')
    name: str = Field(..., description='Name of the campaign', title='Name')
    status: CampaignStatus = Field(..., description='The campaign status')
    startDate: datetime = Field(
        ..., description='Date when the campaign starts', title='Startdate'
    )
    endDate: datetime = Field(
        ..., description='Date when campaign ends', title='Enddate'
    )
    createdAt: datetime = Field(
        ..., description='Time of creation of campaign', title='Createdat'
    )
    ownerUserId: str = Field(
        ..., description='User ID of the campaign owner', title='Owneruserid'
    )
    owner: Optional[UserSchema] = Field(
        default=None, description='User Schema of the campaign owner', title='Owner'
    )


class CampaignSearchFilterBody(BaseModel):
    class Config:
        extra = Extra.forbid

    status: Optional[CampaignStatusFilter] = Field(
        default=None,
        description='Enum: "draft" "initializing" "running" "completed" "failed" "empty" "overdue"\n',
        title='Status',
    )


class Ccm301(BaseModel):
    values: List[Ccm301Standard] = Field(..., description='Values')
    id: Optional[str] = Field(default='ccm301', description='UniqueID', title='Id')
    name: Optional[str] = Field(
        default='CSA STAR (CCM 3.0.1)', description='Name', title='Name'
    )


class Ccm402(BaseModel):
    values: List[Ccm402Standard] = Field(..., description='Values')
    id: Optional[str] = Field(default='ccm402', description='UniqueID', title='Id')
    name: Optional[str] = Field(
        default='CSA STAR (CCM 4.0.2)', description='Name', title='Name'
    )


class Chainable(BaseModel):
    class Config:
        extra = Extra.forbid

    originId: Optional[OriginIdFilter] = Field(
        default=None, description='Origin ID of the Asset.', title='Originid'
    )
    appId: Optional[AppIdFilter] = Field(
        default=None, description='ID of the Application.', title='Appid'
    )
    uniqueId: Optional[UniqueIdFilter] = Field(
        default=None, description='Unique ID of the Asset.', title='Uniqueid'
    )
    authomizeId: Optional[AssetIdFilter] = Field(
        default=None, description='Authomize ID for the Asset', title='Authomizeid'
    )


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(default=None, title='Detail')


class IncidentEntitiesSchema(BaseModel):
    id: str = Field(..., description='Unique id of entity.', title='Id')
    name: Optional[str] = Field(
        default=None, description='Name of entity.', title='Name'
    )
    object: Union[InventoryObjects, str] = Field(
        ..., description='Identity | Account | Asset', title='Object'
    )
    email: Optional[str] = Field(default=None, description='Email', title='Email')
    originId: Optional[str] = Field(
        default=None, description='Origin ID', title='Originid'
    )
    originType: Optional[str] = Field(
        default=None, description='Origin Type', title='Origintype'
    )


class IncidentsSeverityFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    field_in: Optional[List[SeverityType]] = Field(
        default=[], alias='$in', description='In'
    )


class IsoIec27001(BaseModel):
    values: List[IsoIec27001Standard] = Field(..., description='Values')
    id: Optional[str] = Field(default='isoIec27001', description='UniqueID', title='Id')
    name: Optional[str] = Field(
        default='ISO/IEC 27001', description='Name', title='Name'
    )


class NonPaginatedResponseSchemaCampaignSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    data: CampaignSchema = Field(..., description='Actual Data', title='Data')


class PaginatedResponseSchemaAssetSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    pagination: Optional[PaginationResponseSchema] = Field(
        default=None, description='Pagination Metadata', title='Pagination'
    )
    data: List[AssetSchema] = Field(
        ..., description='List of Actual Data', title='Data'
    )


class PaginatedResponseSchemaCampaignSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    pagination: Optional[PaginationResponseSchema] = Field(
        default=None, description='Pagination Metadata', title='Pagination'
    )
    data: List[CampaignSchema] = Field(
        ..., description='List of Actual Data', title='Data'
    )


class RawIdentitySchema(BaseModel):
    authomizeId: str = Field(..., description='Unique ID', title='Authomizeid')
    name: Optional[str] = Field(
        default=None, description='Name of Identity', title='Name'
    )
    title: Optional[str] = Field(default=None, description='Title', title='Title')
    department: Optional[str] = Field(
        default=None, description='Department', title='Department'
    )
    accountIds: Optional[List[str]] = Field(
        default=[], description='List of associated account IDs', title='Accountids'
    )
    email: Optional[str] = Field(
        default=None, description="User's work email address.\n", title='Email'
    )
    tags: Optional[List[TagSchema]] = Field(
        default=None, description='Expanded Tags', title='Tags'
    )
    terminatedAt: Optional[str] = Field(default=None, title='Terminatedat')
    hiredAt: Optional[str] = Field(
        default=None, description='Hired At', title='Hiredat'
    )
    incidentsCount: Optional[int] = Field(
        default=None,
        description='Number of associated incidents',
        title='Incidentscount',
    )


class ReviewerSchema(BaseModel):
    userId: str = Field(..., description='User ID of the Reviewer', title='Userid')
    campaignId: str = Field(..., description='Campaign ID', title='Campaignid')
    lastNotifiedAt: datetime = Field(
        ..., description='Time of last notified', title='Lastnotifiedat'
    )
    lastActiveAt: datetime = Field(
        ..., description='Time of last activity', title='Lastactiveat'
    )
    reviewStatus: Union[ReviewStatus, str] = Field(
        ..., description='Review Status', title='Reviewstatus'
    )
    id: str = Field(..., description='Unique ID', title='Id')
    user: Optional[UserSchema] = Field(
        default=None, description='User Schema of the reviewer', title='User'
    )


class SearchAssetsRequestSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    sort: Optional[List[SortSchemaSearchAssetsSortFields]] = Field(
        default=None, description='Sort', title='Sort'
    )
    pagination: Optional[PaginationRequestSchema] = Field(
        default=None, description='Pagination', title='Pagination'
    )
    expand: Optional[List[AssetExpansion]] = Field(
        default=None, description='Expand Fields'
    )
    filter: Optional[Chainable] = Field(
        default=None, description='Search Assets Filter', title='Filter'
    )


class SearchCampaignPermissionsRequestSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    pagination: Optional[PaginationRequestSchema] = Field(
        default=None, description='Pagination', title='Pagination'
    )
    filter: Optional[CampaignPermissionsSearchFilterBody] = Field(
        default=None, description='Filter by the reviewer decisions. \n', title='Filter'
    )
    expand: Optional[List[PermissionsExpansion]] = Field(
        default=None, description='Fields to expand.\n'
    )


class SearchCampaignsRequestSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    filter: Optional[CampaignSearchFilterBody] = Field(
        default=None, description='Status filter', title='Filter'
    )
    expand: Optional[List[CampaignExpansion]] = Field(
        default=None, description='Expand Fields'
    )
    pagination: Optional[PaginationRequestSchema] = Field(
        default=None, description='Pagination', title='Pagination'
    )
    sort: Optional[List[SortSchemaFieldName]] = Field(
        default=None, description='Sort', title='Sort'
    )


class SearchIdentitiesRequestSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    sort: Optional[List[SortSchemaSearchIdentitiesSortFields]] = Field(
        default=None, description='Sort', title='Sort'
    )
    pagination: Optional[PaginationRequestSchema] = Field(
        default=None, description='Pagination', title='Pagination'
    )
    expand: Optional[List[IdentityExpansion]] = Field(
        default=None, description='Expand Fields'
    )
    filter: Optional[SearchIdentitiesFilterBody] = Field(
        default=None, description='Search Identities Filter', title='Filter'
    )


class SearchIncidentsFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    createdAt: Optional[IncidentsCreatedAtFilter] = Field(
        default=None, description='Created At date', title='Createdat'
    )
    updatedAt: Optional[IncidentsUpdatedAtFilter] = Field(
        default=None, description='Updated At date', title='Updatedat'
    )
    severity: Optional[IncidentsSeverityFilter] = Field(
        default=None, description='Severity', title='Severity'
    )
    status: Optional[IncidentsStatusFilter] = Field(
        default=None, description='Status', title='Status'
    )
    policyId: Optional[IncidentsPolicyIdFilter] = Field(
        default=None, description='Policy Id ', title='Policyid'
    )
    policyTemplateId: Optional[IncidentsPolicyTempalteIdFilter] = Field(
        default=None, description='Policy Template ID', title='Policytemplateid'
    )
    isResolved: Optional[IncidentsIsResolvedFilter] = Field(
        default=None, description='Is resolved?', title='Isresolved'
    )


class SearchIncidentsRequestSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    filter: Optional[SearchIncidentsFilter] = Field(
        default=None, description='Filter', title='Filter'
    )
    expand: Optional[List[IncidentExpansion]] = Field(
        default=None, description='Expend'
    )
    sort: Optional[List[SortSchemaSearchIncidentsSortFields]] = Field(
        default=None, description='Sort', title='Sort'
    )
    pagination: Optional[PaginationRequestSchema] = Field(
        default=None, description='Pagination', title='Pagination'
    )


class AccountSchema(BaseModel):
    authomizeId: str = Field(..., description='Unique ID', title='Authomizeid')
    originId: Optional[str] = Field(
        default=None,
        description='The identifier of the account from the origin system.',
        title='Originid',
    )
    uniqueId: Optional[str] = Field(
        default=None,
        description='Unique ID is an identifier coming from the connector that is guaranteed to be unique across all accounts coming from that connector.',
        title='Uniqueid',
    )
    name: Optional[str] = Field(default=None, description='Name', title='Name')
    type: str = Field(..., description='Type', title='Type')
    isExternal: bool = Field(..., description='Is External', title='Isexternal')
    email: Optional[str] = Field(default=None, description='Email', title='Email')
    identityId: Optional[str] = Field(
        default=None, description='Associated Identity ID ', title='Identityid'
    )
    identity: Optional[RawIdentitySchema] = Field(
        default=None, description='Associated Identity', title='Identity'
    )
    sourceApp: Optional[SourceAppSchema] = Field(
        default=None, description='Source App', title='Sourceapp'
    )
    isAdmin: Optional[bool] = Field(
        default=None, description='Is Admin', title='Isadmin'
    )
    tags: Optional[List[TagSchema]] = Field(
        default=None, description='Expanded Tags', title='Tags'
    )


class CampaignsPermissionSchema(BaseModel):
    id: str = Field(..., description='Campaign ID (unique). \n', title='Id')
    campaignId: str = Field(
        ..., description='ID of the Campaign.\n', title='Campaignid'
    )
    reviewerId: str = Field(..., description='Reviewer ID', title='Reviewerid')
    reviewer: Optional[ReviewerSchema] = Field(
        default=None, description='Details of the reviewer.\n', title='Reviewer'
    )
    actorId: str = Field(
        ...,
        description='Actor ID (Account or Grouping ID) that their access was reviewed. \n',
        title='Actorid',
    )
    actorType: AccessByType = Field(
        ...,
        description='Type of entity that was reviewed, can be Account or Grouping.\n',
    )
    targetId: str = Field(
        ...,
        description='Target ID (Asset or Grouping ID) that the access to was reviewed, for example a database the access to was reviewed.  \n',
        title='Targetid',
    )
    targetType: AccessToType = Field(
        ..., description='Assets or grouping that the access to was reviewed.  \n'
    )
    privilegeId: Optional[str] = Field(
        default=None,
        description='ID of the privileges that was reviewed. \n',
        title='Privilegeid',
    )
    decision: Optional[Selection] = Field(
        default=None, description='Reviewer decisions (keep, revoke or null).\n'
    )
    decisionReason: Optional[str] = Field(
        default=None,
        description='Reviewer decision for keeping or revoking the reviewed access.  \n',
        title='Decisionreason',
    )


class IdentitySchema(BaseModel):
    authomizeId: str = Field(..., description='Unique ID', title='Authomizeid')
    name: Optional[str] = Field(
        default=None, description='Name of Identity', title='Name'
    )
    title: Optional[str] = Field(default=None, description='Title', title='Title')
    department: Optional[str] = Field(
        default=None, description='Department', title='Department'
    )
    accountIds: Optional[List[str]] = Field(
        default=[], description='List of associated account IDs', title='Accountids'
    )
    email: Optional[str] = Field(
        default=None, description="User's work email address.\n", title='Email'
    )
    tags: Optional[List[TagSchema]] = Field(
        default=None, description='Expanded Tags', title='Tags'
    )
    terminatedAt: Optional[str] = Field(default=None, title='Terminatedat')
    hiredAt: Optional[str] = Field(
        default=None, description='Hired At', title='Hiredat'
    )
    incidentsCount: Optional[int] = Field(
        default=None,
        description='Number of associated incidents',
        title='Incidentscount',
    )
    accounts: Optional[List[AccountSchema]] = Field(
        default=[], description='List of associated accounts', title='Accounts'
    )


class IncidentSchema(BaseModel):
    id: str = Field(..., description='Unique id', title='Id')
    createdAt: Optional[datetime] = Field(
        default=None,
        description='The date the incident was first reported.',
        title='Createdat',
    )
    updatedAt: Optional[datetime] = Field(
        default=None,
        description='The date the incident was last updated.',
        title='Updatedat',
    )
    entities: Optional[List[IncidentEntitiesSchema]] = Field(
        default=[], description='Entity', title='Entities'
    )
    apps: Optional[List[SourceAppSchema]] = Field(
        default=[], description='Applications', title='Apps'
    )
    category: Optional[AlertCategoryType] = Field(default=None, description='Category')
    tactics: Optional[List[AttackTacticType]] = Field(default=[], description='Tactics')
    compliance: Optional[
        List[Union[IsoIec27001, AicpaTsc2017, Ccm402, Ccm301, Cisv8]]
    ] = Field(default=[], description='Compliance', title='Compliance')
    techniques: Optional[List[str]] = Field(
        default=[], description='Techniques', title='Techniques'
    )
    status: Optional[EventStatusType] = Field(
        default=None,
        description='The status of the incident (Open, In Progress, Waiting for Input, or Closed)',
    )
    severity: SeverityType = Field(
        ..., description='The severity of the incident (Low, Medium, High or Critical).'
    )
    policyId: str = Field(..., description='Unique id of policy.', title='Policyid')
    policy: Optional[PolicySchema] = Field(
        default=None, description='Policy', title='Policy'
    )
    assigneeId: Optional[str] = Field(
        default=None, description='Unique id of assignee.', title='Assigneeid'
    )
    assignee: Optional[UserSchema] = Field(
        default=None, description='Assignee', title='Assignee'
    )
    recommendation: Optional[str] = Field(
        default=None, description='Recommendation', title='Recommendation'
    )
    description: Optional[str] = Field(
        default=None, description='Description', title='Description'
    )
    isResolved: bool = Field(..., description='Is Resolved?', title='Isresolved')
    url: str = Field(..., description='URL', title='Url')


class NonPaginatedResponseSchemaIncidentSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    data: IncidentSchema = Field(..., description='Actual Data', title='Data')


class NonPaginatedResponseSchemaReviewerSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    data: ReviewerSchema = Field(..., description='Actual Data', title='Data')


class PaginatedResponseSchemaCampaignsPermissionSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    pagination: Optional[PaginationResponseSchema] = Field(
        default=None, description='Pagination Metadata', title='Pagination'
    )
    data: List[CampaignsPermissionSchema] = Field(
        ..., description='List of Actual Data', title='Data'
    )


class PaginatedResponseSchemaIdentitySchema(BaseModel):
    class Config:
        extra = Extra.forbid

    pagination: Optional[PaginationResponseSchema] = Field(
        default=None, description='Pagination Metadata', title='Pagination'
    )
    data: List[IdentitySchema] = Field(
        ..., description='List of Actual Data', title='Data'
    )


class PaginatedResponseSchemaIncidentSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    pagination: Optional[PaginationResponseSchema] = Field(
        default=None, description='Pagination Metadata', title='Pagination'
    )
    data: List[IncidentSchema] = Field(
        ..., description='List of Actual Data', title='Data'
    )
