def check_metadata(document, metadata_filters):
    """
    Check whether document metadata matches the filters.
    """

    metadata = document.get("metadata", {})

    for key, value in metadata_filters.items():

        if metadata.get(key) != value:
            return False

    return True


def check_user_groups(document, user_groups):
    """
    Check whether the user shares an authorized group
    with the document.
    """

    allowed_groups = document.get("allowed_groups", [])

    return bool(set(user_groups) & set(allowed_groups))


def check_acl_permission(document, user_id, required_permission):
    """
    Check whether the user has the required ACL permission.
    """

    acl = document.get("acl", {})

    user_permissions = acl.get(user_id, [])

    return required_permission in user_permissions


def metadata_filter(
    documents,
    user,
    metadata_filters=None,
    required_permission="read"
):
    """
    Filter documents using metadata, user groups and ACL.
    """

    if metadata_filters is None:
        metadata_filters = {}

    user_id = user.get("user_id")
    user_groups = user.get("groups", [])

    if not user_id:
        raise ValueError("User ID is required")

    filtered_documents = []

    for document in documents:

        # Step 1: Metadata filtering
        if not check_metadata(document, metadata_filters):
            continue

        # Step 2: User group filtering
        if not check_user_groups(document, user_groups):
            continue

        # Step 3: ACL permission filtering
        if not check_acl_permission(
            document,
            user_id,
            required_permission
        ):
            continue

        filtered_documents.append(document)

    return filtered_documents


if __name__ == "__main__":

    documents = [

        {
            "id": "doc_101",
            "content": "HR leave policy",
            "metadata": {
                "department": "HR",
                "document_type": "policy"
            },
            "allowed_groups": ["HR", "MANAGER"],
            "acl": {
                "user_101": ["read", "write"],
                "user_102": ["read"]
            }
        },

        {
            "id": "doc_102",
            "content": "Finance salary report",
            "metadata": {
                "department": "FINANCE",
                "document_type": "report"
            },
            "allowed_groups": ["FINANCE"],
            "acl": {
                "user_101": ["read"]
            }
        },

        {
            "id": "doc_103",
            "content": "HR confidential employee data",
            "metadata": {
                "department": "HR",
                "document_type": "confidential"
            },
            "allowed_groups": ["HR"],
            "acl": {
                "user_102": ["read", "write"]
            }
        },

        {
            "id": "doc_104",
            "content": "HR recruitment policy",
            "metadata": {
                "department": "HR",
                "document_type": "policy"
            },
            "allowed_groups": ["HR"],
            "acl": {
                "user_101": ["read"]
            }
        }
    ]

    user = {
        "user_id": "user_101",
        "groups": ["HR"],
        "role": "employee"
    }

    metadata_filters = {
        "department": "HR",
        "document_type": "policy"
    }

    results = metadata_filter(
        documents=documents,
        user=user,
        metadata_filters=metadata_filters,
        required_permission="read"
    )

    print("Authorized Documents:")

    for document in results:
        print(document["id"], ":", document["content"])