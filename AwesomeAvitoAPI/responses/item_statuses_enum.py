import enum


class ItemStatus(enum.Enum):
    ACTIVE = 'active'
    REMOVED = 'removed'
    OLD = 'old'
    BLOCKED = 'blocked'
    REJECTED = 'rejected'
