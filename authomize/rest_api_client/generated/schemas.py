# generated by datamodel-codegen:
#   filename:  openapi.json
#   timestamp: 2021-12-26T09:07:02+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class ActorType(Enum):
    Authomize = 'Authomize'
    User = 'User'


class AssetsInheritance(BaseModel):
    fromId: str = Field(..., title='Fromid')
    toId: str = Field(..., title='Toid')


class AvailableConnectorId(Enum):
    aws = 'aws'
    box = 'box'
    dropbox = 'dropbox'
    fileprovider = 'fileprovider'
    github = 'github'
    google = 'google'
    jira = 'jira'
    microsoft_azure_ad_sp = 'microsoft-azure-ad-sp'
    microsoft_azure = 'microsoft-azure'
    okta = 'okta'
    oktaOwners = 'oktaOwners'
    restApiImport = 'restApiImport'
    salesforce_application = 'salesforce_application'
    salesforce_account = 'salesforce_account'
    jiraServiceDeskItsm = 'jiraServiceDeskItsm'


class CanonicalPrivilegeTypes(Enum):
    Unknown = 'Unknown'
    All = 'All'
    Owner = 'Owner'
    Read = 'Read'
    ReadMetadata = 'ReadMetadata'
    Write = 'Write'
    Create = 'Create'
    Delete = 'Delete'
    Execute = 'Execute'
    Enable = 'Enable'
    Assign = 'Assign'
    Restore = 'Restore'
    Import = 'Import'
    Export = 'Export'
    Get = 'Get'
    Set = 'Set'
    Update = 'Update'
    Cancel = 'Cancel'
    Use = 'Use'
    AllowUse = 'AllowUse'
    List = 'List'
    Administrative = 'Administrative'
    Delegate = 'Delegate'
    Join = 'Join'
    Invite = 'Invite'
    Leave = 'Leave'
    Share = 'Share'


class ConnectorStatus(Enum):
    enabled = 'enabled'
    disabled = 'disabled'
    installable = 'installable'


class ExportResponse(BaseModel):
    exportId: str = Field(..., title='Exportid')
    exportUrl: str = Field(..., title='Exporturl')


class IdentitiesInheritance(BaseModel):
    fromId: str = Field(..., title='Fromid')
    toId: str = Field(..., title='Toid')


class IdentityTypes(Enum):
    Identity = 'Identity'
    User = 'User'
    Group = 'Group'
    EntitlementProxy = 'EntitlementProxy'
    AccessKey = 'AccessKey'
    ServiceAccount = 'ServiceAccount'
    Alias = 'Alias'
    Domain = 'Domain'
    Organization = 'Organization'
    TaskPerformer = 'TaskPerformer'


class IsAliveResponse(BaseModel):
    isAlive: bool = Field(..., title='Isalive')


class MeResponse(BaseModel):
    version: str = Field(..., title='Version')
    id: str = Field(..., title='Id')
    tenant: str = Field(..., title='Tenant')


class NewRestApiConnectorSchema(BaseModel):
    config: Optional[Dict[str, Any]] = Field(None, title='Config')
    serviceId: Optional[str] = Field(None, title='Serviceid')


class ResourceTypes(Enum):
    Resource = 'Resource'
    File = 'File'
    Folder = 'Folder'
    Drive = 'Drive'
    Site = 'Site'
    Application = 'Application'
    Package = 'Package'
    Project = 'Project'
    Cluster = 'Cluster'
    Dataset = 'Dataset'
    Subscription = 'Subscription'
    Table = 'Table'
    TableRecord = 'TableRecord'
    Disk = 'Disk'
    Image = 'Image'
    Instance = 'Instance'
    Snapshot = 'Snapshot'
    Service = 'Service'
    Topic = 'Topic'
    Bucket = 'Bucket'
    BillingAccount = 'BillingAccount'
    Device = 'Device'
    Calendar = 'Calendar'
    Policy = 'Policy'
    GitRepository = 'GitRepository'
    Network = 'Network'
    Vpc = 'Vpc'
    NetworkInterface = 'NetworkInterface'
    VirtualMachine = 'VirtualMachine'
    NetworkSecurityGroup = 'NetworkSecurityGroup'
    Ticket = 'Ticket'
    NetworkSubnet = 'NetworkSubnet'
    NetworkAcl = 'NetworkAcl'
    RouteTable = 'RouteTable'
    NetworkAddress = 'NetworkAddress'
    Secret = 'Secret'
    Storage = 'Storage'
    Workspace = 'Workspace'
    SharedLink = 'SharedLink'
    Collection = 'Collection'
    Resource_Domain = 'Resource_Domain'
    Resource_Organization = 'Resource_Organization'
    Resource_Group = 'Resource_Group'
    Resource_ServiceAccount = 'Resource_ServiceAccount'
    Resource_User = 'Resource_User'
    Resource_Identity = 'Resource_Identity'
    Resource_EntitlementProxy = 'Resource_EntitlementProxy'
    Resource_AccessKey = 'Resource_AccessKey'
    Resource_TaskPerformer = 'Resource_TaskPerformer'
    Database = 'Database'


class RestApiImportServicesType(Enum):
    RestApiImport = 'RestApiImport'


class ServiceDescription(BaseModel):
    name: str = Field(..., title='Name')
    icon: Optional[str] = Field(None, title='Icon')


class SubmitResponse(BaseModel):
    acceptedTimestamp: datetime = Field(..., title='Acceptedtimestamp')


class TransactionStateType(Enum):
    Complete = 'Complete'
    Failed = 'Failed'
    Ingest = 'Ingest'
    IngestChunk = 'IngestChunk'
    PostProcess = 'PostProcess'
    Queue = 'Queue'


class TransactionType(Enum):
    Insert = 'Insert'


class UserStatus(Enum):
    Staged = 'Staged'
    Enabled = 'Enabled'
    Disabled = 'Disabled'
    Suspended = 'Suspended'
    Deleted = 'Deleted'


class ValidationError(BaseModel):
    loc: List[str] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class AuthomizeArangoStoresModelsPagination(BaseModel):
    total: int = Field(..., title='Total')
    limit: int = Field(..., title='Limit')
    skip: int = Field(..., title='Skip')


class AuthomizeClientsSchemasPluginsServicePluginsServicePagination(BaseModel):
    limit: Optional[int] = Field(-1, title='Limit')
    skip: Optional[int] = Field(0, title='Skip')
    total: Optional[int] = Field(-1, title='Total')


class AccessDescription(BaseModel):
    fromIdentityId: str = Field(..., title='Fromidentityid')
    toAssetId: str = Field(..., title='Toassetid')
    accessType: CanonicalPrivilegeTypes
    accessName: Optional[str] = Field(None, title='Accessname')


class AssetDescription(BaseModel):
    id: str = Field(..., title='Id')
    name: str = Field(..., title='Name')
    type: ResourceTypes
    description: Optional[str] = Field(None, title='Description')
    href: Optional[str] = Field(None, title='Href')
    createdAt: Optional[datetime] = Field(None, title='Createdat')
    service: Optional[str] = Field(None, title='Service')


class BundleTransaction(BaseModel):
    transactionCreatedAt: Optional[datetime] = Field(None, title='Transactioncreatedat')
    transactionLastInsertionAt: Optional[datetime] = Field(None, title='Transactionlastinsertionat')
    transactionUpdatedAt: Optional[datetime] = Field(None, title='Transactionupdatedat')
    actorId: Optional[str] = Field(None, title='Actorid')
    actorType: Optional[ActorType] = None
    sourceKey: str = Field(..., title='Sourcekey')
    connectorId: str = Field(..., title='Connectorid')
    transactionType: Optional[TransactionType] = None
    origin: Optional[str] = Field(None, title='Origin')
    warnings: Optional[List[str]] = Field(None, title='Warnings')
    id: str = Field(..., title='Id')
    state: TransactionStateType


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')


class IdentityDescription(BaseModel):
    id: str = Field(..., title='Id')
    name: str = Field(..., title='Name')
    type: IdentityTypes
    email: Optional[str] = Field(None, title='Email')
    manager: Optional[str] = Field(None, title='Manager')
    title: Optional[str] = Field(None, title='Title')
    description: Optional[str] = Field(None, title='Description')
    href: Optional[str] = Field(None, title='Href')
    createdAt: Optional[datetime] = Field(None, title='Createdat')
    terminationDate: Optional[datetime] = Field(None, title='Terminationdate')
    isExternal: Optional[bool] = Field(None, title='Isexternal')
    hasTwoFactorAuthenticationEnabled: Optional[bool] = Field(
        None, title='Hastwofactorauthenticationenabled'
    )
    firstName: Optional[str] = Field(None, title='Firstname')
    lastName: Optional[str] = Field(None, title='Lastname')
    userName: Optional[str] = Field(None, title='Username')
    status: Optional[UserStatus] = None
    service: Optional[str] = Field(None, title='Service')


class ItemsBundleSchema(BaseModel):
    services: List[ServiceDescription] = Field(..., title='Services')
    identities: List[IdentityDescription] = Field(..., title='Identities')
    assets: List[AssetDescription] = Field(..., title='Assets')
    inheritanceIdentities: List[IdentitiesInheritance] = Field(..., title='Inheritanceidentities')
    inheritanceAssets: List[AssetsInheritance] = Field(..., title='Inheritanceassets')
    access: List[AccessDescription] = Field(..., title='Access')


class RestApiConnectorSchema(BaseModel):
    config: Optional[Dict[str, Any]] = Field(None, title='Config')
    serviceId: Optional[str] = Field(None, title='Serviceid')
    id: str = Field(..., title='Id')
    createdAt: Optional[str] = Field(None, title='Createdat')
    lastSyncedAt: Optional[str] = Field(None, title='Lastsyncedat')
    lastError: Optional[str] = Field(None, title='Lasterror')
    modifiedAt: Optional[str] = Field(None, title='Modifiedat')
    status: Optional[ConnectorStatus] = 'disabled'
    serviceType: Optional[RestApiImportServicesType] = 'RestApiImport'
    availableConnectorId: Optional[AvailableConnectorId] = 'restApiImport'
    actorType: Optional[str] = Field(None, title='Actortype')
    actorId: Optional[str] = Field(None, title='Actorid')


class TransactionPaginatedSearchSchema(BaseModel):
    data: List[BundleTransaction] = Field(..., title='Data')
    pagination: AuthomizeArangoStoresModelsPagination


class RestApiConnectorListSchema(BaseModel):
    pagination: AuthomizeClientsSchemasPluginsServicePluginsServicePagination
    data: List[RestApiConnectorSchema] = Field(..., title='Data')
