#!/usr/bin/env python

def cast_value_as_defaults_output(type, value):
    if type == 'string' or type == 'int' or type == 'integer' or type == 'float':
        return '' + value
    elif type == 'bool' or type == 'boolean':
        if value:
            return '1'
        else:
            return '0'
    else:
        # not supported especially; such as a `array`. see also `man defaults`
        return '' + value

def write_defaults(module, name, domain, type, value):
    module.run_command(["defaults", "write", domain, name, "-" + type, value], check_rc = True)

def delete_defaults(module, name, domain):
    module.run_command(["defaults", "delete", domain, name], check_rc = True)

# => stdout: Maybe<string>
def read_defaults(module, name, domain):
    rc, stdout, _=module.run_command(["defaults", "read", domain, name])
    if rc != 0: # failure
        return None
    else:
        return stdout

# => results: dict
def ensure_present(module, name, domain, type, value):
    current=read_defaults(module=module, name=name, domain=domain)
    if current == None or current.strip() != cast_value_as_defaults_output(type = type, value = value): # should write the value
        write_defaults(module=module, name=name, domain=domain, type=type, value=value)
        return { 'changed': True }
    else:
        return { 'changed': False }

def ensure_absent(module, name, domain):
    current=read_defaults(module=module, name=name, domain=domain)
    if current == None:
        return { 'changed': False }
    else:
        delete_defaults(module=module, name=name, domain=domain)

def main():
    module=AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str'),
            state=dict(required=False, type='str', default='present'), # present or absent
            domain=dict(required=True, type='str'),
            type=dict(required=False, type='str', default = 'string'),
            value=dict(required=True, type='str'),
        ),
    )
    if module.params['state'] == 'present':
        results=ensure_present(
            module=module,
            name = module.params['name'],
            domain = module.params['domain'],
            type = module.params['type'],
            value = module.params['value'])
        module.exit_json(**results)
    elif module.params['state'] == 'absent':
        results=ensure_absent(
            module=module,
            name = module.params['name'],
            domain = module.params['domain'])
        module.exit_json(**results)

from ansible.module_utils.basic import *
main()
