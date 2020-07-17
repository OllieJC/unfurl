import re


email_edge = {
    "color": {"color": "lightgreen"},
    "title": "Email Parsing Functions",
    "label": "@",
}


def run(unfurl, node):
    if not isinstance(node.value, str):
        return

    r = re.compile(r"(?i)^[\w\-%&'+`]{1,64}@[a-z0-9\.\-]{1,255}\.[a-z]{2,4}$")

    if "@" in node.value and not node.data_type == "email" and r.match(node.value):
        email = node.value.strip()
        unfurl.add_to_queue(
            data_type="email",
            key=None,
            label=f"{email}",
            value=email,
            hover="Email address, per "
            '<a href="https://tools.ietf.org/html/rfc5321" target="_blank">RFC5321</a>',
            parent_id=node.node_id,
            incoming_edge_config=email_edge,
        )

    if node.data_type == "email" and r.match(node.value):
        email = node.value.strip()
        email_split = email.split("@")
        email_local = email_split[0]
        email_domain = email_split[1]

        unfurl.add_to_queue(
            data_type="url",
            key=None,
            value=email_local,
            label=f"Local-part: {email_local}",
            hover="Email local-part, per "
            '<a href="https://tools.ietf.org/html/rfc5321#section-4.5.3.1.1" target="_blank">RFC5321#section-4.5.3.1.1</a>',
            parent_id=node.node_id,
            incoming_edge_config=email_edge,
        )

        unfurl.add_to_queue(
            data_type="url.hostname",
            key=None,
            value=email_domain,
            label=f"Domain: {email_domain}",
            hover="Email domain, per "
            '<a href="https://tools.ietf.org/html/rfc5321#section-4.5.3.1.2" target="_blank">RFC5321#section-4.5.3.1.2</a>',
            parent_id=node.node_id,
            incoming_edge_config=email_edge,
        )
