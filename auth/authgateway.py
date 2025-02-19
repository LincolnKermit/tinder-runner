# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: authgateway.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

import betterproto


class LoginResultCaptcha(betterproto.Enum):
    CAPTCHA_INVALID = 0
    CAPTCHA_V1 = 1
    CAPTCHA_V2 = 2


class SocialConnectionService(betterproto.Enum):
    SERVICE_INVALID = 0
    SERVICE_FACEBOOK = 1
    SERVICE_GOOGLE = 2
    SERVICE_APPLE = 3


@dataclass
class MetaProto(betterproto.Message):
    upstream_time: datetime = betterproto.message_field(1)
    start_time: datetime = betterproto.message_field(2)


@dataclass
class GetPhoneState(betterproto.Message):
    refresh_token: Optional[str] = betterproto.message_field(
        1, wraps=betterproto.TYPE_STRING
    )


@dataclass
class ValidatePhoneOtpState(betterproto.Message):
    refresh_token: Optional[str] = betterproto.message_field(
        1, wraps=betterproto.TYPE_STRING
    )
    phone: str = betterproto.string_field(2)
    otp_length: Optional[int] = betterproto.message_field(
        3, wraps=betterproto.TYPE_INT32
    )
    sms_sent: Optional[bool] = betterproto.message_field(4, wraps=betterproto.TYPE_BOOL)


@dataclass
class EmailMarketing(betterproto.Message):
    show_marketing_opt_in: Optional[bool] = betterproto.message_field(
        2, wraps=betterproto.TYPE_BOOL
    )
    show_strict_opt_in: Optional[bool] = betterproto.message_field(
        3, wraps=betterproto.TYPE_BOOL
    )
    checked_by_default: Optional[bool] = betterproto.message_field(
        4, wraps=betterproto.TYPE_BOOL
    )


@dataclass
class GetEmailState(betterproto.Message):
    refresh_token: Optional[str] = betterproto.message_field(
        1, wraps=betterproto.TYPE_STRING
    )
    email_marketing: "EmailMarketing" = betterproto.message_field(2)


@dataclass
class ValidateEmailOtpState(betterproto.Message):
    refresh_token: Optional[str] = betterproto.message_field(
        1, wraps=betterproto.TYPE_STRING
    )
    otp_length: Optional[int] = betterproto.message_field(
        4, wraps=betterproto.TYPE_INT32
    )
    email_sent: Optional[bool] = betterproto.message_field(
        5, wraps=betterproto.TYPE_BOOL
    )
    email_marketing: "EmailMarketing" = betterproto.message_field(6)
    unmasked_email: str = betterproto.string_field(2, group="email")
    masked_email: str = betterproto.string_field(3, group="email")


@dataclass
class OnboardingState(betterproto.Message):
    refresh_token: str = betterproto.string_field(1)
    onboarding_token: str = betterproto.string_field(2)
    user_id: Optional[str] = betterproto.message_field(3, wraps=betterproto.TYPE_STRING)


@dataclass
class LoginResult(betterproto.Message):
    refresh_token: str = betterproto.string_field(1)
    auth_token: str = betterproto.string_field(2)
    captcha: "LoginResultCaptcha" = betterproto.enum_field(3)
    user_id: str = betterproto.string_field(4)
    auth_token_ttl: Optional[int] = betterproto.message_field(
        5, wraps=betterproto.TYPE_INT64
    )


@dataclass
class AppleAccountNotFound(betterproto.Message):
    will_link: bool = betterproto.bool_field(1)
    refresh_token: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )


@dataclass
class SocialConnection(betterproto.Message):
    service: "SocialConnectionService" = betterproto.enum_field(1)


@dataclass
class SocialConnectionList(betterproto.Message):
    refresh_token: Optional[str] = betterproto.message_field(
        1, wraps=betterproto.TYPE_STRING
    )
    connections: List["SocialConnection"] = betterproto.message_field(2)


@dataclass
class ValidateEmailMagicLinkOtpState(betterproto.Message):
    pass


@dataclass
class AuthGatewayResponse(betterproto.Message):
    meta: "MetaProto" = betterproto.message_field(1)
    error: "ErrorProto" = betterproto.message_field(2)
    get_phone_state: "GetPhoneState" = betterproto.message_field(3, group="data")
    validate_phone_otp_state: "ValidatePhoneOtpState" = betterproto.message_field(
        4, group="data"
    )
    get_email_state: "GetEmailState" = betterproto.message_field(5, group="data")
    validate_email_otp_state: "ValidateEmailOtpState" = betterproto.message_field(
        6, group="data"
    )
    onboarding_state: "OnboardingState" = betterproto.message_field(7, group="data")
    login_result: "LoginResult" = betterproto.message_field(8, group="data")
    social_connection_list: "SocialConnectionList" = betterproto.message_field(
        9, group="data"
    )
    apple_account_not_found: "AppleAccountNotFound" = betterproto.message_field(
        10, group="data"
    )
    validate_email_magic_link_otp_state: "ValidateEmailMagicLinkOtpState" = betterproto.message_field(
        11, group="data"
    )


@dataclass
class FacebookToken(betterproto.Message):
    external_token: str = betterproto.string_field(1)
    refresh_token: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )


@dataclass
class Phone(betterproto.Message):
    phone: str = betterproto.string_field(1)
    refresh_token: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )
    captcha_token: Optional[str] = betterproto.message_field(
        3, group="check", wraps=betterproto.TYPE_STRING
    )
    ios_device_token: Optional[str] = betterproto.message_field(
        4, group="check", wraps=betterproto.TYPE_STRING
    )
    android_jws: Optional[str] = betterproto.message_field(
        5, group="check", wraps=betterproto.TYPE_STRING
    )


@dataclass
class PhoneOtpResend(betterproto.Message):
    phone: Optional[str] = betterproto.message_field(1, wraps=betterproto.TYPE_STRING)
    refresh_token: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )
    ios_device_token: Optional[str] = betterproto.message_field(
        3, group="check", wraps=betterproto.TYPE_STRING
    )
    android_jws: Optional[str] = betterproto.message_field(
        4, group="check", wraps=betterproto.TYPE_STRING
    )


@dataclass
class PhoneOtp(betterproto.Message):
    phone: Optional[str] = betterproto.message_field(1, wraps=betterproto.TYPE_STRING)
    otp: str = betterproto.string_field(2)
    refresh_token: Optional[str] = betterproto.message_field(
        3, wraps=betterproto.TYPE_STRING
    )


@dataclass
class Email(betterproto.Message):
    email: str = betterproto.string_field(1)
    refresh_token: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )
    marketing_opt_in: Optional[bool] = betterproto.message_field(
        3, wraps=betterproto.TYPE_BOOL
    )


@dataclass
class EmailOtpResend(betterproto.Message):
    email: Optional[str] = betterproto.message_field(1, wraps=betterproto.TYPE_STRING)
    refresh_token: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )


@dataclass
class GoogleToken(betterproto.Message):
    external_token: str = betterproto.string_field(1)
    refresh_token: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )
    marketing_opt_in: Optional[bool] = betterproto.message_field(
        3, wraps=betterproto.TYPE_BOOL
    )
    user_behavior: Optional[bool] = betterproto.message_field(
        4, wraps=betterproto.TYPE_BOOL
    )


@dataclass
class EmailOtp(betterproto.Message):
    email: Optional[str] = betterproto.message_field(1, wraps=betterproto.TYPE_STRING)
    otp: str = betterproto.string_field(2)
    refresh_token: Optional[str] = betterproto.message_field(
        3, wraps=betterproto.TYPE_STRING
    )


@dataclass
class AppleToken(betterproto.Message):
    external_token: str = betterproto.string_field(1)
    refresh_token: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )
    raw_nonce: Optional[str] = betterproto.message_field(
        3, wraps=betterproto.TYPE_STRING
    )


@dataclass
class GetInitialState(betterproto.Message):
    refresh_token: Optional[str] = betterproto.message_field(
        1, wraps=betterproto.TYPE_STRING
    )


@dataclass
class RefreshAuth(betterproto.Message):
    refresh_token: str = betterproto.string_field(1)


@dataclass
class DismissSocialConnectionList(betterproto.Message):
    refresh_token: str = betterproto.string_field(1)


@dataclass
class EmailMagicLink(betterproto.Message):
    email: str = betterproto.string_field(1)


@dataclass
class EmailMagicLinkOtp(betterproto.Message):
    otp_token: str = betterproto.string_field(1)


@dataclass
class AuthGatewayRequest(betterproto.Message):
    phone: "Phone" = betterproto.message_field(1, group="factor")
    phone_otp: "PhoneOtp" = betterproto.message_field(2, group="factor")
    email: "Email" = betterproto.message_field(3, group="factor")
    google_token: "GoogleToken" = betterproto.message_field(4, group="factor")
    email_otp: "EmailOtp" = betterproto.message_field(5, group="factor")
    facebook_token: "FacebookToken" = betterproto.message_field(6, group="factor")
    phone_otp_resend: "PhoneOtpResend" = betterproto.message_field(7, group="factor")
    email_otp_resend: "EmailOtpResend" = betterproto.message_field(8, group="factor")
    get_initial_state: "GetInitialState" = betterproto.message_field(9, group="factor")
    refresh_auth: "RefreshAuth" = betterproto.message_field(10, group="factor")
    apple_token: "AppleToken" = betterproto.message_field(11, group="factor")
    dismiss_social_connection_list: "DismissSocialConnectionList" = betterproto.message_field(
        12, group="factor"
    )
    email_magic_link: "EmailMagicLink" = betterproto.message_field(13, group="factor")
    email_magic_link_otp: "EmailMagicLinkOtp" = betterproto.message_field(
        14, group="factor"
    )


@dataclass
class Verification(betterproto.Message):
    type: str = betterproto.string_field(1)
    state: str = betterproto.string_field(2)


@dataclass
class UnderageBan(betterproto.Message):
    underage_ttl_duration_ms: Optional[int] = betterproto.message_field(
        1, wraps=betterproto.TYPE_INT64
    )
    underage_token: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )
    verification: "Verification" = betterproto.message_field(3)


@dataclass
class BanAppeal(betterproto.Message):
    challenge_type: str = betterproto.string_field(1)
    challenge_token: str = betterproto.string_field(2)
    refresh_token: str = betterproto.string_field(3)


@dataclass
class BanReason(betterproto.Message):
    underage_ban: "UnderageBan" = betterproto.message_field(1, group="reason")
    ban_appeal: "BanAppeal" = betterproto.message_field(2, group="reason")


@dataclass
class ErrorProto(betterproto.Message):
    code: int = betterproto.int32_field(1)
    message: str = betterproto.string_field(2)
    ban_reason: "BanReason" = betterproto.message_field(3)
