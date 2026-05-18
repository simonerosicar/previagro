from app.utils.exceptions import ValidationError


def _validate_string_field(name, value, required=True, min_len=2, max_len=100):
    if value is None:
        if required:
            raise ValidationError(f"Campo '{name}' é obrigatório")
        return None

    if not isinstance(value, str):
        raise ValidationError(f"Campo '{name}' deve ser uma string")

    value = value.strip()
    if required and not value:
        raise ValidationError(f"Campo '{name}' não pode estar vazio")

    if value and len(value) < min_len:
        raise ValidationError(f"Campo '{name}' deve ter pelo menos {min_len} caracteres")
    if value and len(value) > max_len:
        raise ValidationError(f"Campo '{name}' deve ter no máximo {max_len} caracteres")

    return value


def _validate_bool_field(name, value, required=False):
    if value is None:
        if required:
            raise ValidationError(f"Campo '{name}' é obrigatório")
        return None

    if isinstance(value, bool):
        return value

    if isinstance(value, str):
        lower = value.lower()
        if lower in {"true", "1", "sim", "yes"}:
            return True
        if lower in {"false", "0", "nao", "não", "no"}:
            return False

    raise ValidationError(f"Campo '{name}' deve ser booleano")


def validate_produtor_payload(payload, partial=False):
    if not isinstance(payload, dict):
        raise ValidationError("Payload deve ser um objeto JSON")

    nome = payload.get("nome")
    cidade = payload.get("cidade")
    ativo = payload.get("ativo")

    if partial:
        if nome is not None:
            nome = _validate_string_field("nome", nome, required=False)
        if cidade is not None:
            cidade = _validate_string_field("cidade", cidade, required=False)
    else:
        nome = _validate_string_field("nome", nome, required=True)
        cidade = _validate_string_field("cidade", cidade, required=True)

    if ativo is not None:
        ativo = _validate_bool_field("ativo", ativo, required=False)

    return {
        "nome": nome,
        "cidade": cidade,
        "ativo": ativo,
    }


def validate_login_payload(payload):
    if not isinstance(payload, dict):
        raise ValidationError("Payload deve ser um objeto JSON")

    username = _validate_string_field("username", payload.get("username"), required=True)
    password = _validate_string_field("password", payload.get("password"), required=True, min_len=6)
    return {"username": username, "password": password}


def validate_user_payload(payload):
    if not isinstance(payload, dict):
        raise ValidationError("Payload deve ser um objeto JSON")

    username = _validate_string_field("username", payload.get("username"), required=True, min_len=3, max_len=80)
    password = _validate_string_field("password", payload.get("password"), required=True, min_len=6)
    return {"username": username, "password": password}
