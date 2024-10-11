# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: etcd3/etcdrpc/rpc.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'etcd3/etcdrpc/rpc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from etcd3.etcdrpc import kv_pb2 as etcd3_dot_etcdrpc_dot_kv__pb2
from etcd3.etcdrpc import auth_pb2 as etcd3_dot_etcdrpc_dot_auth__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x65tcd3/etcdrpc/rpc.proto\x12\x11\x65tcd3.etcdrpc.rpc\x1a\x16\x65tcd3/etcdrpc/kv.proto\x1a\x18\x65tcd3/etcdrpc/auth.proto\"\\\n\x0eResponseHeader\x12\x12\n\ncluster_id\x18\x01 \x01(\x04\x12\x11\n\tmember_id\x18\x02 \x01(\x04\x12\x10\n\x08revision\x18\x03 \x01(\x03\x12\x11\n\traft_term\x18\x04 \x01(\x04\"\xee\x03\n\x0cRangeRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x11\n\trange_end\x18\x02 \x01(\x0c\x12\r\n\x05limit\x18\x03 \x01(\x03\x12\x10\n\x08revision\x18\x04 \x01(\x03\x12=\n\nsort_order\x18\x05 \x01(\x0e\x32).etcd3.etcdrpc.rpc.RangeRequest.SortOrder\x12?\n\x0bsort_target\x18\x06 \x01(\x0e\x32*.etcd3.etcdrpc.rpc.RangeRequest.SortTarget\x12\x14\n\x0cserializable\x18\x07 \x01(\x08\x12\x11\n\tkeys_only\x18\x08 \x01(\x08\x12\x12\n\ncount_only\x18\t \x01(\x08\x12\x18\n\x10min_mod_revision\x18\n \x01(\x03\x12\x18\n\x10max_mod_revision\x18\x0b \x01(\x03\x12\x1b\n\x13min_create_revision\x18\x0c \x01(\x03\x12\x1b\n\x13max_create_revision\x18\r \x01(\x03\".\n\tSortOrder\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06\x41SCEND\x10\x01\x12\x0b\n\x07\x44\x45SCEND\x10\x02\"B\n\nSortTarget\x12\x07\n\x03KEY\x10\x00\x12\x0b\n\x07VERSION\x10\x01\x12\n\n\x06\x43REATE\x10\x02\x12\x07\n\x03MOD\x10\x03\x12\t\n\x05VALUE\x10\x04\"\x88\x01\n\rRangeResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\'\n\x03kvs\x18\x02 \x03(\x0b\x32\x1a.etcd3.etcdrpc.kv.KeyValue\x12\x0c\n\x04more\x18\x03 \x01(\x08\x12\r\n\x05\x63ount\x18\x04 \x01(\x03\"t\n\nPutRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\r\n\x05lease\x18\x03 \x01(\x03\x12\x0f\n\x07prev_kv\x18\x04 \x01(\x08\x12\x14\n\x0cignore_value\x18\x05 \x01(\x08\x12\x14\n\x0cignore_lease\x18\x06 \x01(\x08\"m\n\x0bPutResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12+\n\x07prev_kv\x18\x02 \x01(\x0b\x32\x1a.etcd3.etcdrpc.kv.KeyValue\"E\n\x12\x44\x65leteRangeRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x11\n\trange_end\x18\x02 \x01(\x0c\x12\x0f\n\x07prev_kv\x18\x03 \x01(\x08\"\x87\x01\n\x13\x44\x65leteRangeResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\x0f\n\x07\x64\x65leted\x18\x02 \x01(\x03\x12,\n\x08prev_kvs\x18\x03 \x03(\x0b\x32\x1a.etcd3.etcdrpc.kv.KeyValue\"\x83\x02\n\tRequestOp\x12\x38\n\rrequest_range\x18\x01 \x01(\x0b\x32\x1f.etcd3.etcdrpc.rpc.RangeRequestH\x00\x12\x34\n\x0brequest_put\x18\x02 \x01(\x0b\x32\x1d.etcd3.etcdrpc.rpc.PutRequestH\x00\x12\x45\n\x14request_delete_range\x18\x03 \x01(\x0b\x32%.etcd3.etcdrpc.rpc.DeleteRangeRequestH\x00\x12\x34\n\x0brequest_txn\x18\x04 \x01(\x0b\x32\x1d.etcd3.etcdrpc.rpc.TxnRequestH\x00\x42\t\n\x07request\"\x8d\x02\n\nResponseOp\x12:\n\x0eresponse_range\x18\x01 \x01(\x0b\x32 .etcd3.etcdrpc.rpc.RangeResponseH\x00\x12\x36\n\x0cresponse_put\x18\x02 \x01(\x0b\x32\x1e.etcd3.etcdrpc.rpc.PutResponseH\x00\x12G\n\x15response_delete_range\x18\x03 \x01(\x0b\x32&.etcd3.etcdrpc.rpc.DeleteRangeResponseH\x00\x12\x36\n\x0cresponse_txn\x18\x04 \x01(\x0b\x32\x1e.etcd3.etcdrpc.rpc.TxnResponseH\x00\x42\n\n\x08response\"\xa0\x03\n\x07\x43ompare\x12\x38\n\x06result\x18\x01 \x01(\x0e\x32(.etcd3.etcdrpc.rpc.Compare.CompareResult\x12\x38\n\x06target\x18\x02 \x01(\x0e\x32(.etcd3.etcdrpc.rpc.Compare.CompareTarget\x12\x0b\n\x03key\x18\x03 \x01(\x0c\x12\x11\n\x07version\x18\x04 \x01(\x03H\x00\x12\x19\n\x0f\x63reate_revision\x18\x05 \x01(\x03H\x00\x12\x16\n\x0cmod_revision\x18\x06 \x01(\x03H\x00\x12\x0f\n\x05value\x18\x07 \x01(\x0cH\x00\x12\x0f\n\x05lease\x18\x08 \x01(\x03H\x00\x12\x11\n\trange_end\x18@ \x01(\x0c\"@\n\rCompareResult\x12\t\n\x05\x45QUAL\x10\x00\x12\x0b\n\x07GREATER\x10\x01\x12\x08\n\x04LESS\x10\x02\x12\r\n\tNOT_EQUAL\x10\x03\"G\n\rCompareTarget\x12\x0b\n\x07VERSION\x10\x00\x12\n\n\x06\x43REATE\x10\x01\x12\x07\n\x03MOD\x10\x02\x12\t\n\x05VALUE\x10\x03\x12\t\n\x05LEASE\x10\x04\x42\x0e\n\x0ctarget_union\"\x97\x01\n\nTxnRequest\x12+\n\x07\x63ompare\x18\x01 \x03(\x0b\x32\x1a.etcd3.etcdrpc.rpc.Compare\x12-\n\x07success\x18\x02 \x03(\x0b\x32\x1c.etcd3.etcdrpc.rpc.RequestOp\x12-\n\x07\x66\x61ilure\x18\x03 \x03(\x0b\x32\x1c.etcd3.etcdrpc.rpc.RequestOp\"\x85\x01\n\x0bTxnResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\x11\n\tsucceeded\x18\x02 \x01(\x08\x12\x30\n\tresponses\x18\x03 \x03(\x0b\x32\x1d.etcd3.etcdrpc.rpc.ResponseOp\"7\n\x11\x43ompactionRequest\x12\x10\n\x08revision\x18\x01 \x01(\x03\x12\x10\n\x08physical\x18\x02 \x01(\x08\"G\n\x12\x43ompactionResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"\r\n\x0bHashRequest\"O\n\x0cHashResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\x0c\n\x04hash\x18\x02 \x01(\r\"!\n\rHashKVRequest\x12\x10\n\x08revision\x18\x01 \x01(\x03\"k\n\x0eHashKVResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\x0c\n\x04hash\x18\x02 \x01(\r\x12\x18\n\x10\x63ompact_revision\x18\x03 \x01(\x03\"\x11\n\x0fSnapshotRequest\"l\n\x10SnapshotResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\x17\n\x0fremaining_bytes\x18\x02 \x01(\x04\x12\x0c\n\x04\x62lob\x18\x03 \x01(\x0c\"\xe6\x01\n\x0cWatchRequest\x12?\n\x0e\x63reate_request\x18\x01 \x01(\x0b\x32%.etcd3.etcdrpc.rpc.WatchCreateRequestH\x00\x12?\n\x0e\x63\x61ncel_request\x18\x02 \x01(\x0b\x32%.etcd3.etcdrpc.rpc.WatchCancelRequestH\x00\x12\x43\n\x10progress_request\x18\x03 \x01(\x0b\x32\'.etcd3.etcdrpc.rpc.WatchProgressRequestH\x00\x42\x0f\n\rrequest_union\"\xe0\x01\n\x12WatchCreateRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x11\n\trange_end\x18\x02 \x01(\x0c\x12\x16\n\x0estart_revision\x18\x03 \x01(\x03\x12\x17\n\x0fprogress_notify\x18\x04 \x01(\x08\x12\x41\n\x07\x66ilters\x18\x05 \x03(\x0e\x32\x30.etcd3.etcdrpc.rpc.WatchCreateRequest.FilterType\x12\x0f\n\x07prev_kv\x18\x06 \x01(\x08\"%\n\nFilterType\x12\t\n\x05NOPUT\x10\x00\x12\x0c\n\x08NODELETE\x10\x01\"&\n\x12WatchCancelRequest\x12\x10\n\x08watch_id\x18\x01 \x01(\x03\"\x16\n\x14WatchProgressRequest\"\xd1\x01\n\rWatchResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\x10\n\x08watch_id\x18\x02 \x01(\x03\x12\x0f\n\x07\x63reated\x18\x03 \x01(\x08\x12\x10\n\x08\x63\x61nceled\x18\x04 \x01(\x08\x12\x18\n\x10\x63ompact_revision\x18\x05 \x01(\x03\x12\x15\n\rcancel_reason\x18\x06 \x01(\t\x12\'\n\x06\x65vents\x18\x0b \x03(\x0b\x32\x17.etcd3.etcdrpc.kv.Event\",\n\x11LeaseGrantRequest\x12\x0b\n\x03TTL\x18\x01 \x01(\x03\x12\n\n\x02ID\x18\x02 \x01(\x03\"o\n\x12LeaseGrantResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\n\n\x02ID\x18\x02 \x01(\x03\x12\x0b\n\x03TTL\x18\x03 \x01(\x03\x12\r\n\x05\x65rror\x18\x04 \x01(\t\" \n\x12LeaseRevokeRequest\x12\n\n\x02ID\x18\x01 \x01(\x03\"H\n\x13LeaseRevokeResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"#\n\x15LeaseKeepAliveRequest\x12\n\n\x02ID\x18\x01 \x01(\x03\"d\n\x16LeaseKeepAliveResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\n\n\x02ID\x18\x02 \x01(\x03\x12\x0b\n\x03TTL\x18\x03 \x01(\x03\"2\n\x16LeaseTimeToLiveRequest\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x0c\n\x04keys\x18\x02 \x01(\x08\"\x87\x01\n\x17LeaseTimeToLiveResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\n\n\x02ID\x18\x02 \x01(\x03\x12\x0b\n\x03TTL\x18\x03 \x01(\x03\x12\x12\n\ngrantedTTL\x18\x04 \x01(\x03\x12\x0c\n\x04keys\x18\x05 \x03(\x0c\"H\n\x06Member\x12\n\n\x02ID\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08peerURLs\x18\x03 \x03(\t\x12\x12\n\nclientURLs\x18\x04 \x03(\t\"$\n\x10MemberAddRequest\x12\x10\n\x08peerURLs\x18\x01 \x03(\t\"\x9d\x01\n\x11MemberAddResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12)\n\x06member\x18\x02 \x01(\x0b\x32\x19.etcd3.etcdrpc.rpc.Member\x12*\n\x07members\x18\x03 \x03(\x0b\x32\x19.etcd3.etcdrpc.rpc.Member\"!\n\x13MemberRemoveRequest\x12\n\n\x02ID\x18\x01 \x01(\x04\"u\n\x14MemberRemoveResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12*\n\x07members\x18\x02 \x03(\x0b\x32\x19.etcd3.etcdrpc.rpc.Member\"3\n\x13MemberUpdateRequest\x12\n\n\x02ID\x18\x01 \x01(\x04\x12\x10\n\x08peerURLs\x18\x02 \x03(\t\"u\n\x14MemberUpdateResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12*\n\x07members\x18\x02 \x03(\x0b\x32\x19.etcd3.etcdrpc.rpc.Member\"\x13\n\x11MemberListRequest\"s\n\x12MemberListResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12*\n\x07members\x18\x02 \x03(\x0b\x32\x19.etcd3.etcdrpc.rpc.Member\"\x13\n\x11\x44\x65\x66ragmentRequest\"G\n\x12\x44\x65\x66ragmentResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"%\n\x11MoveLeaderRequest\x12\x10\n\x08targetID\x18\x01 \x01(\x04\"G\n\x12MoveLeaderResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"\xc0\x01\n\x0c\x41larmRequest\x12;\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32+.etcd3.etcdrpc.rpc.AlarmRequest.AlarmAction\x12\x10\n\x08memberID\x18\x02 \x01(\x04\x12+\n\x05\x61larm\x18\x03 \x01(\x0e\x32\x1c.etcd3.etcdrpc.rpc.AlarmType\"4\n\x0b\x41larmAction\x12\x07\n\x03GET\x10\x00\x12\x0c\n\x08\x41\x43TIVATE\x10\x01\x12\x0e\n\nDEACTIVATE\x10\x02\"L\n\x0b\x41larmMember\x12\x10\n\x08memberID\x18\x01 \x01(\x04\x12+\n\x05\x61larm\x18\x02 \x01(\x0e\x32\x1c.etcd3.etcdrpc.rpc.AlarmType\"r\n\rAlarmResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12.\n\x06\x61larms\x18\x02 \x03(\x0b\x32\x1e.etcd3.etcdrpc.rpc.AlarmMember\"\x0f\n\rStatusRequest\"\x99\x01\n\x0eStatusResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x62Size\x18\x03 \x01(\x03\x12\x0e\n\x06leader\x18\x04 \x01(\x04\x12\x11\n\traftIndex\x18\x05 \x01(\x04\x12\x10\n\x08raftTerm\x18\x06 \x01(\x04\"\x13\n\x11\x41uthEnableRequest\"\x14\n\x12\x41uthDisableRequest\"5\n\x13\x41uthenticateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"4\n\x12\x41uthUserAddRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\"\n\x12\x41uthUserGetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"%\n\x15\x41uthUserDeleteRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"?\n\x1d\x41uthUserChangePasswordRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"6\n\x18\x41uthUserGrantRoleRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\"7\n\x19\x41uthUserRevokeRoleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\"\"\n\x12\x41uthRoleAddRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\"\n\x12\x41uthRoleGetRequest\x12\x0c\n\x04role\x18\x01 \x01(\t\"\x15\n\x13\x41uthUserListRequest\"\x15\n\x13\x41uthRoleListRequest\"%\n\x15\x41uthRoleDeleteRequest\x12\x0c\n\x04role\x18\x01 \x01(\t\"\\\n\x1e\x41uthRoleGrantPermissionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x04perm\x18\x02 \x01(\x0b\x32\x1e.etcd3.etcdrpc.auth.Permission\"O\n\x1f\x41uthRoleRevokePermissionRequest\x12\x0c\n\x04role\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x11\n\trange_end\x18\x03 \x01(\t\"G\n\x12\x41uthEnableResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"H\n\x13\x41uthDisableResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"X\n\x14\x41uthenticateResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\r\n\x05token\x18\x02 \x01(\t\"H\n\x13\x41uthUserAddResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"W\n\x13\x41uthUserGetResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\r\n\x05roles\x18\x02 \x03(\t\"K\n\x16\x41uthUserDeleteResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"S\n\x1e\x41uthUserChangePasswordResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"N\n\x19\x41uthUserGrantRoleResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"O\n\x1a\x41uthUserRevokeRoleResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"H\n\x13\x41uthRoleAddResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"v\n\x13\x41uthRoleGetResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12,\n\x04perm\x18\x02 \x03(\x0b\x32\x1e.etcd3.etcdrpc.auth.Permission\"X\n\x14\x41uthRoleListResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\r\n\x05roles\x18\x02 \x03(\t\"X\n\x14\x41uthUserListResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\x12\r\n\x05users\x18\x02 \x03(\t\"K\n\x16\x41uthRoleDeleteResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"T\n\x1f\x41uthRoleGrantPermissionResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader\"U\n AuthRoleRevokePermissionResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.etcd3.etcdrpc.rpc.ResponseHeader*\"\n\tAlarmType\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07NOSPACE\x10\x01\x32\x9c\x03\n\x02KV\x12L\n\x05Range\x12\x1f.etcd3.etcdrpc.rpc.RangeRequest\x1a .etcd3.etcdrpc.rpc.RangeResponse\"\x00\x12\x46\n\x03Put\x12\x1d.etcd3.etcdrpc.rpc.PutRequest\x1a\x1e.etcd3.etcdrpc.rpc.PutResponse\"\x00\x12^\n\x0b\x44\x65leteRange\x12%.etcd3.etcdrpc.rpc.DeleteRangeRequest\x1a&.etcd3.etcdrpc.rpc.DeleteRangeResponse\"\x00\x12\x46\n\x03Txn\x12\x1d.etcd3.etcdrpc.rpc.TxnRequest\x1a\x1e.etcd3.etcdrpc.rpc.TxnResponse\"\x00\x12X\n\x07\x43ompact\x12$.etcd3.etcdrpc.rpc.CompactionRequest\x1a%.etcd3.etcdrpc.rpc.CompactionResponse\"\x00\x32\xb2\x01\n\x05Watch\x12W\n\x08Progress\x12\'.etcd3.etcdrpc.rpc.WatchProgressRequest\x1a .etcd3.etcdrpc.rpc.WatchResponse\"\x00\x12P\n\x05Watch\x12\x1f.etcd3.etcdrpc.rpc.WatchRequest\x1a .etcd3.etcdrpc.rpc.WatchResponse\"\x00(\x01\x30\x01\x32\x9d\x03\n\x05Lease\x12[\n\nLeaseGrant\x12$.etcd3.etcdrpc.rpc.LeaseGrantRequest\x1a%.etcd3.etcdrpc.rpc.LeaseGrantResponse\"\x00\x12^\n\x0bLeaseRevoke\x12%.etcd3.etcdrpc.rpc.LeaseRevokeRequest\x1a&.etcd3.etcdrpc.rpc.LeaseRevokeResponse\"\x00\x12k\n\x0eLeaseKeepAlive\x12(.etcd3.etcdrpc.rpc.LeaseKeepAliveRequest\x1a).etcd3.etcdrpc.rpc.LeaseKeepAliveResponse\"\x00(\x01\x30\x01\x12j\n\x0fLeaseTimeToLive\x12).etcd3.etcdrpc.rpc.LeaseTimeToLiveRequest\x1a*.etcd3.etcdrpc.rpc.LeaseTimeToLiveResponse\"\x00\x32\x86\x03\n\x07\x43luster\x12X\n\tMemberAdd\x12#.etcd3.etcdrpc.rpc.MemberAddRequest\x1a$.etcd3.etcdrpc.rpc.MemberAddResponse\"\x00\x12\x61\n\x0cMemberRemove\x12&.etcd3.etcdrpc.rpc.MemberRemoveRequest\x1a\'.etcd3.etcdrpc.rpc.MemberRemoveResponse\"\x00\x12\x61\n\x0cMemberUpdate\x12&.etcd3.etcdrpc.rpc.MemberUpdateRequest\x1a\'.etcd3.etcdrpc.rpc.MemberUpdateResponse\"\x00\x12[\n\nMemberList\x12$.etcd3.etcdrpc.rpc.MemberListRequest\x1a%.etcd3.etcdrpc.rpc.MemberListResponse\"\x00\x32\xdb\x04\n\x0bMaintenance\x12L\n\x05\x41larm\x12\x1f.etcd3.etcdrpc.rpc.AlarmRequest\x1a .etcd3.etcdrpc.rpc.AlarmResponse\"\x00\x12O\n\x06Status\x12 .etcd3.etcdrpc.rpc.StatusRequest\x1a!.etcd3.etcdrpc.rpc.StatusResponse\"\x00\x12[\n\nDefragment\x12$.etcd3.etcdrpc.rpc.DefragmentRequest\x1a%.etcd3.etcdrpc.rpc.DefragmentResponse\"\x00\x12I\n\x04Hash\x12\x1e.etcd3.etcdrpc.rpc.HashRequest\x1a\x1f.etcd3.etcdrpc.rpc.HashResponse\"\x00\x12O\n\x06HashKV\x12 .etcd3.etcdrpc.rpc.HashKVRequest\x1a!.etcd3.etcdrpc.rpc.HashKVResponse\"\x00\x12W\n\x08Snapshot\x12\".etcd3.etcdrpc.rpc.SnapshotRequest\x1a#.etcd3.etcdrpc.rpc.SnapshotResponse\"\x00\x30\x01\x12[\n\nMoveLeader\x12$.etcd3.etcdrpc.rpc.MoveLeaderRequest\x1a%.etcd3.etcdrpc.rpc.MoveLeaderResponse\"\x00\x32\xfe\x0c\n\x04\x41uth\x12[\n\nAuthEnable\x12$.etcd3.etcdrpc.rpc.AuthEnableRequest\x1a%.etcd3.etcdrpc.rpc.AuthEnableResponse\"\x00\x12^\n\x0b\x41uthDisable\x12%.etcd3.etcdrpc.rpc.AuthDisableRequest\x1a&.etcd3.etcdrpc.rpc.AuthDisableResponse\"\x00\x12\x61\n\x0c\x41uthenticate\x12&.etcd3.etcdrpc.rpc.AuthenticateRequest\x1a\'.etcd3.etcdrpc.rpc.AuthenticateResponse\"\x00\x12Z\n\x07UserAdd\x12%.etcd3.etcdrpc.rpc.AuthUserAddRequest\x1a&.etcd3.etcdrpc.rpc.AuthUserAddResponse\"\x00\x12Z\n\x07UserGet\x12%.etcd3.etcdrpc.rpc.AuthUserGetRequest\x1a&.etcd3.etcdrpc.rpc.AuthUserGetResponse\"\x00\x12]\n\x08UserList\x12&.etcd3.etcdrpc.rpc.AuthUserListRequest\x1a\'.etcd3.etcdrpc.rpc.AuthUserListResponse\"\x00\x12\x63\n\nUserDelete\x12(.etcd3.etcdrpc.rpc.AuthUserDeleteRequest\x1a).etcd3.etcdrpc.rpc.AuthUserDeleteResponse\"\x00\x12{\n\x12UserChangePassword\x12\x30.etcd3.etcdrpc.rpc.AuthUserChangePasswordRequest\x1a\x31.etcd3.etcdrpc.rpc.AuthUserChangePasswordResponse\"\x00\x12l\n\rUserGrantRole\x12+.etcd3.etcdrpc.rpc.AuthUserGrantRoleRequest\x1a,.etcd3.etcdrpc.rpc.AuthUserGrantRoleResponse\"\x00\x12o\n\x0eUserRevokeRole\x12,.etcd3.etcdrpc.rpc.AuthUserRevokeRoleRequest\x1a-.etcd3.etcdrpc.rpc.AuthUserRevokeRoleResponse\"\x00\x12Z\n\x07RoleAdd\x12%.etcd3.etcdrpc.rpc.AuthRoleAddRequest\x1a&.etcd3.etcdrpc.rpc.AuthRoleAddResponse\"\x00\x12Z\n\x07RoleGet\x12%.etcd3.etcdrpc.rpc.AuthRoleGetRequest\x1a&.etcd3.etcdrpc.rpc.AuthRoleGetResponse\"\x00\x12]\n\x08RoleList\x12&.etcd3.etcdrpc.rpc.AuthRoleListRequest\x1a\'.etcd3.etcdrpc.rpc.AuthRoleListResponse\"\x00\x12\x63\n\nRoleDelete\x12(.etcd3.etcdrpc.rpc.AuthRoleDeleteRequest\x1a).etcd3.etcdrpc.rpc.AuthRoleDeleteResponse\"\x00\x12~\n\x13RoleGrantPermission\x12\x31.etcd3.etcdrpc.rpc.AuthRoleGrantPermissionRequest\x1a\x32.etcd3.etcdrpc.rpc.AuthRoleGrantPermissionResponse\"\x00\x12\x81\x01\n\x14RoleRevokePermission\x12\x32.etcd3.etcdrpc.rpc.AuthRoleRevokePermissionRequest\x1a\x33.etcd3.etcdrpc.rpc.AuthRoleRevokePermissionResponse\"\x00\x42)\n\x11io.etcd.jetcd.apiB\nJetcdProtoP\x01\xa2\x02\x05Jetcdb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'etcd3.etcdrpc.rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021io.etcd.jetcd.apiB\nJetcdProtoP\001\242\002\005Jetcd'
  _globals['_ALARMTYPE']._serialized_start=7926
  _globals['_ALARMTYPE']._serialized_end=7960
  _globals['_RESPONSEHEADER']._serialized_start=96
  _globals['_RESPONSEHEADER']._serialized_end=188
  _globals['_RANGEREQUEST']._serialized_start=191
  _globals['_RANGEREQUEST']._serialized_end=685
  _globals['_RANGEREQUEST_SORTORDER']._serialized_start=571
  _globals['_RANGEREQUEST_SORTORDER']._serialized_end=617
  _globals['_RANGEREQUEST_SORTTARGET']._serialized_start=619
  _globals['_RANGEREQUEST_SORTTARGET']._serialized_end=685
  _globals['_RANGERESPONSE']._serialized_start=688
  _globals['_RANGERESPONSE']._serialized_end=824
  _globals['_PUTREQUEST']._serialized_start=826
  _globals['_PUTREQUEST']._serialized_end=942
  _globals['_PUTRESPONSE']._serialized_start=944
  _globals['_PUTRESPONSE']._serialized_end=1053
  _globals['_DELETERANGEREQUEST']._serialized_start=1055
  _globals['_DELETERANGEREQUEST']._serialized_end=1124
  _globals['_DELETERANGERESPONSE']._serialized_start=1127
  _globals['_DELETERANGERESPONSE']._serialized_end=1262
  _globals['_REQUESTOP']._serialized_start=1265
  _globals['_REQUESTOP']._serialized_end=1524
  _globals['_RESPONSEOP']._serialized_start=1527
  _globals['_RESPONSEOP']._serialized_end=1796
  _globals['_COMPARE']._serialized_start=1799
  _globals['_COMPARE']._serialized_end=2215
  _globals['_COMPARE_COMPARERESULT']._serialized_start=2062
  _globals['_COMPARE_COMPARERESULT']._serialized_end=2126
  _globals['_COMPARE_COMPARETARGET']._serialized_start=2128
  _globals['_COMPARE_COMPARETARGET']._serialized_end=2199
  _globals['_TXNREQUEST']._serialized_start=2218
  _globals['_TXNREQUEST']._serialized_end=2369
  _globals['_TXNRESPONSE']._serialized_start=2372
  _globals['_TXNRESPONSE']._serialized_end=2505
  _globals['_COMPACTIONREQUEST']._serialized_start=2507
  _globals['_COMPACTIONREQUEST']._serialized_end=2562
  _globals['_COMPACTIONRESPONSE']._serialized_start=2564
  _globals['_COMPACTIONRESPONSE']._serialized_end=2635
  _globals['_HASHREQUEST']._serialized_start=2637
  _globals['_HASHREQUEST']._serialized_end=2650
  _globals['_HASHRESPONSE']._serialized_start=2652
  _globals['_HASHRESPONSE']._serialized_end=2731
  _globals['_HASHKVREQUEST']._serialized_start=2733
  _globals['_HASHKVREQUEST']._serialized_end=2766
  _globals['_HASHKVRESPONSE']._serialized_start=2768
  _globals['_HASHKVRESPONSE']._serialized_end=2875
  _globals['_SNAPSHOTREQUEST']._serialized_start=2877
  _globals['_SNAPSHOTREQUEST']._serialized_end=2894
  _globals['_SNAPSHOTRESPONSE']._serialized_start=2896
  _globals['_SNAPSHOTRESPONSE']._serialized_end=3004
  _globals['_WATCHREQUEST']._serialized_start=3007
  _globals['_WATCHREQUEST']._serialized_end=3237
  _globals['_WATCHCREATEREQUEST']._serialized_start=3240
  _globals['_WATCHCREATEREQUEST']._serialized_end=3464
  _globals['_WATCHCREATEREQUEST_FILTERTYPE']._serialized_start=3427
  _globals['_WATCHCREATEREQUEST_FILTERTYPE']._serialized_end=3464
  _globals['_WATCHCANCELREQUEST']._serialized_start=3466
  _globals['_WATCHCANCELREQUEST']._serialized_end=3504
  _globals['_WATCHPROGRESSREQUEST']._serialized_start=3506
  _globals['_WATCHPROGRESSREQUEST']._serialized_end=3528
  _globals['_WATCHRESPONSE']._serialized_start=3531
  _globals['_WATCHRESPONSE']._serialized_end=3740
  _globals['_LEASEGRANTREQUEST']._serialized_start=3742
  _globals['_LEASEGRANTREQUEST']._serialized_end=3786
  _globals['_LEASEGRANTRESPONSE']._serialized_start=3788
  _globals['_LEASEGRANTRESPONSE']._serialized_end=3899
  _globals['_LEASEREVOKEREQUEST']._serialized_start=3901
  _globals['_LEASEREVOKEREQUEST']._serialized_end=3933
  _globals['_LEASEREVOKERESPONSE']._serialized_start=3935
  _globals['_LEASEREVOKERESPONSE']._serialized_end=4007
  _globals['_LEASEKEEPALIVEREQUEST']._serialized_start=4009
  _globals['_LEASEKEEPALIVEREQUEST']._serialized_end=4044
  _globals['_LEASEKEEPALIVERESPONSE']._serialized_start=4046
  _globals['_LEASEKEEPALIVERESPONSE']._serialized_end=4146
  _globals['_LEASETIMETOLIVEREQUEST']._serialized_start=4148
  _globals['_LEASETIMETOLIVEREQUEST']._serialized_end=4198
  _globals['_LEASETIMETOLIVERESPONSE']._serialized_start=4201
  _globals['_LEASETIMETOLIVERESPONSE']._serialized_end=4336
  _globals['_MEMBER']._serialized_start=4338
  _globals['_MEMBER']._serialized_end=4410
  _globals['_MEMBERADDREQUEST']._serialized_start=4412
  _globals['_MEMBERADDREQUEST']._serialized_end=4448
  _globals['_MEMBERADDRESPONSE']._serialized_start=4451
  _globals['_MEMBERADDRESPONSE']._serialized_end=4608
  _globals['_MEMBERREMOVEREQUEST']._serialized_start=4610
  _globals['_MEMBERREMOVEREQUEST']._serialized_end=4643
  _globals['_MEMBERREMOVERESPONSE']._serialized_start=4645
  _globals['_MEMBERREMOVERESPONSE']._serialized_end=4762
  _globals['_MEMBERUPDATEREQUEST']._serialized_start=4764
  _globals['_MEMBERUPDATEREQUEST']._serialized_end=4815
  _globals['_MEMBERUPDATERESPONSE']._serialized_start=4817
  _globals['_MEMBERUPDATERESPONSE']._serialized_end=4934
  _globals['_MEMBERLISTREQUEST']._serialized_start=4936
  _globals['_MEMBERLISTREQUEST']._serialized_end=4955
  _globals['_MEMBERLISTRESPONSE']._serialized_start=4957
  _globals['_MEMBERLISTRESPONSE']._serialized_end=5072
  _globals['_DEFRAGMENTREQUEST']._serialized_start=5074
  _globals['_DEFRAGMENTREQUEST']._serialized_end=5093
  _globals['_DEFRAGMENTRESPONSE']._serialized_start=5095
  _globals['_DEFRAGMENTRESPONSE']._serialized_end=5166
  _globals['_MOVELEADERREQUEST']._serialized_start=5168
  _globals['_MOVELEADERREQUEST']._serialized_end=5205
  _globals['_MOVELEADERRESPONSE']._serialized_start=5207
  _globals['_MOVELEADERRESPONSE']._serialized_end=5278
  _globals['_ALARMREQUEST']._serialized_start=5281
  _globals['_ALARMREQUEST']._serialized_end=5473
  _globals['_ALARMREQUEST_ALARMACTION']._serialized_start=5421
  _globals['_ALARMREQUEST_ALARMACTION']._serialized_end=5473
  _globals['_ALARMMEMBER']._serialized_start=5475
  _globals['_ALARMMEMBER']._serialized_end=5551
  _globals['_ALARMRESPONSE']._serialized_start=5553
  _globals['_ALARMRESPONSE']._serialized_end=5667
  _globals['_STATUSREQUEST']._serialized_start=5669
  _globals['_STATUSREQUEST']._serialized_end=5684
  _globals['_STATUSRESPONSE']._serialized_start=5687
  _globals['_STATUSRESPONSE']._serialized_end=5840
  _globals['_AUTHENABLEREQUEST']._serialized_start=5842
  _globals['_AUTHENABLEREQUEST']._serialized_end=5861
  _globals['_AUTHDISABLEREQUEST']._serialized_start=5863
  _globals['_AUTHDISABLEREQUEST']._serialized_end=5883
  _globals['_AUTHENTICATEREQUEST']._serialized_start=5885
  _globals['_AUTHENTICATEREQUEST']._serialized_end=5938
  _globals['_AUTHUSERADDREQUEST']._serialized_start=5940
  _globals['_AUTHUSERADDREQUEST']._serialized_end=5992
  _globals['_AUTHUSERGETREQUEST']._serialized_start=5994
  _globals['_AUTHUSERGETREQUEST']._serialized_end=6028
  _globals['_AUTHUSERDELETEREQUEST']._serialized_start=6030
  _globals['_AUTHUSERDELETEREQUEST']._serialized_end=6067
  _globals['_AUTHUSERCHANGEPASSWORDREQUEST']._serialized_start=6069
  _globals['_AUTHUSERCHANGEPASSWORDREQUEST']._serialized_end=6132
  _globals['_AUTHUSERGRANTROLEREQUEST']._serialized_start=6134
  _globals['_AUTHUSERGRANTROLEREQUEST']._serialized_end=6188
  _globals['_AUTHUSERREVOKEROLEREQUEST']._serialized_start=6190
  _globals['_AUTHUSERREVOKEROLEREQUEST']._serialized_end=6245
  _globals['_AUTHROLEADDREQUEST']._serialized_start=6247
  _globals['_AUTHROLEADDREQUEST']._serialized_end=6281
  _globals['_AUTHROLEGETREQUEST']._serialized_start=6283
  _globals['_AUTHROLEGETREQUEST']._serialized_end=6317
  _globals['_AUTHUSERLISTREQUEST']._serialized_start=6319
  _globals['_AUTHUSERLISTREQUEST']._serialized_end=6340
  _globals['_AUTHROLELISTREQUEST']._serialized_start=6342
  _globals['_AUTHROLELISTREQUEST']._serialized_end=6363
  _globals['_AUTHROLEDELETEREQUEST']._serialized_start=6365
  _globals['_AUTHROLEDELETEREQUEST']._serialized_end=6402
  _globals['_AUTHROLEGRANTPERMISSIONREQUEST']._serialized_start=6404
  _globals['_AUTHROLEGRANTPERMISSIONREQUEST']._serialized_end=6496
  _globals['_AUTHROLEREVOKEPERMISSIONREQUEST']._serialized_start=6498
  _globals['_AUTHROLEREVOKEPERMISSIONREQUEST']._serialized_end=6577
  _globals['_AUTHENABLERESPONSE']._serialized_start=6579
  _globals['_AUTHENABLERESPONSE']._serialized_end=6650
  _globals['_AUTHDISABLERESPONSE']._serialized_start=6652
  _globals['_AUTHDISABLERESPONSE']._serialized_end=6724
  _globals['_AUTHENTICATERESPONSE']._serialized_start=6726
  _globals['_AUTHENTICATERESPONSE']._serialized_end=6814
  _globals['_AUTHUSERADDRESPONSE']._serialized_start=6816
  _globals['_AUTHUSERADDRESPONSE']._serialized_end=6888
  _globals['_AUTHUSERGETRESPONSE']._serialized_start=6890
  _globals['_AUTHUSERGETRESPONSE']._serialized_end=6977
  _globals['_AUTHUSERDELETERESPONSE']._serialized_start=6979
  _globals['_AUTHUSERDELETERESPONSE']._serialized_end=7054
  _globals['_AUTHUSERCHANGEPASSWORDRESPONSE']._serialized_start=7056
  _globals['_AUTHUSERCHANGEPASSWORDRESPONSE']._serialized_end=7139
  _globals['_AUTHUSERGRANTROLERESPONSE']._serialized_start=7141
  _globals['_AUTHUSERGRANTROLERESPONSE']._serialized_end=7219
  _globals['_AUTHUSERREVOKEROLERESPONSE']._serialized_start=7221
  _globals['_AUTHUSERREVOKEROLERESPONSE']._serialized_end=7300
  _globals['_AUTHROLEADDRESPONSE']._serialized_start=7302
  _globals['_AUTHROLEADDRESPONSE']._serialized_end=7374
  _globals['_AUTHROLEGETRESPONSE']._serialized_start=7376
  _globals['_AUTHROLEGETRESPONSE']._serialized_end=7494
  _globals['_AUTHROLELISTRESPONSE']._serialized_start=7496
  _globals['_AUTHROLELISTRESPONSE']._serialized_end=7584
  _globals['_AUTHUSERLISTRESPONSE']._serialized_start=7586
  _globals['_AUTHUSERLISTRESPONSE']._serialized_end=7674
  _globals['_AUTHROLEDELETERESPONSE']._serialized_start=7676
  _globals['_AUTHROLEDELETERESPONSE']._serialized_end=7751
  _globals['_AUTHROLEGRANTPERMISSIONRESPONSE']._serialized_start=7753
  _globals['_AUTHROLEGRANTPERMISSIONRESPONSE']._serialized_end=7837
  _globals['_AUTHROLEREVOKEPERMISSIONRESPONSE']._serialized_start=7839
  _globals['_AUTHROLEREVOKEPERMISSIONRESPONSE']._serialized_end=7924
  _globals['_KV']._serialized_start=7963
  _globals['_KV']._serialized_end=8375
  _globals['_WATCH']._serialized_start=8378
  _globals['_WATCH']._serialized_end=8556
  _globals['_LEASE']._serialized_start=8559
  _globals['_LEASE']._serialized_end=8972
  _globals['_CLUSTER']._serialized_start=8975
  _globals['_CLUSTER']._serialized_end=9365
  _globals['_MAINTENANCE']._serialized_start=9368
  _globals['_MAINTENANCE']._serialized_end=9971
  _globals['_AUTH']._serialized_start=9974
  _globals['_AUTH']._serialized_end=11636
# @@protoc_insertion_point(module_scope)
