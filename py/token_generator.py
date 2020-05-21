import json
import uuid
import base64

redis = None


class TokenGenerator:
    """ 通过 gen_token 生成一个token，通过try_use_token尝试消费一个token。
    token_type, token的业务含义，比如登录校验、邮箱校验等
    input_raw, 表示用户填写的值，用于生成token。
    input_b64, input_raw base64之后的值

    gen_token: 参数相同时，复用现有的token
    get_input_raw: 将input_b64还原成原始的input_raw
    try_use_token: 当token校验通过时，消费token, 否则表示token非法，不消耗token。
    """

    @staticmethod
    def _key(token_type, input_b64):
        return f"token_generator#{token_type}#{input_b64}"

    @staticmethod
    def _get_token(token_type, input_b64):
        key = TokenGenerator._key(token_type, input_b64)
        json_value = (redis.get(key) or b"").decode()
        if not json_value:
            return None
        return json.loads(json_value).get("token")

    @staticmethod
    def get_input_raw(input_b64):
        return base64.urlsafe_b64decode(input_b64).decode()

    @staticmethod
    def gen_token(token_type, input_raw, ttl=24 * 60 * 60):
        """ return input_b64, token"""
        input_b64 = base64.urlsafe_b64encode(input_raw.encode("utf-8"))
        token = TokenGenerator._get_token(token_type, input_b64)
        if token:
            return input_b64, token
        token = uuid.uuid4().hex
        json_value = json.dumps({"token": token})
        key = TokenGenerator._key(token_type, input_b64)
        if redis.set(key, json_value, nx=True, ex=ttl):
            return input_b64, token
        return input_b64, TokenGenerator._get_token(token_type, input_b64)

    @staticmethod
    def try_use_token(token_type, input_b64, token):
        if TokenGenerator._get_token(token_type, input_b64) != token:
            return False
        key = TokenGenerator._key(token_type, input_b64)
        return bool(redis.delete(key))
