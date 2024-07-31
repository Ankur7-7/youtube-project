SSL_CA = '/opt/python/rds-combined-ca-bundle.pem'
CASH_FREE_BANK_TYPE = 5


class Env:
    DEV = "development"
    STAGE = "staging"
    PREPROD = "preprod"
    PROD = "production"


class SettlementStatus:
    INITIATED = "INITIATED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
