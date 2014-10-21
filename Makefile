ANSIBLE_PLAYBOOK_CMD         = ansible-playbook
ANSIBLE_LOCAL_INVENTORY_FILE = inventories/local
ANSIBLE_LOCAL_PLAYBOOK_FILE  = local.yml

run: run-playbook-local

run-playbook-local:
	$(ANSIBLE_PLAYBOOK_CMD) -i $(ANSIBLE_LOCAL_INVENTORY_FILE) $(ANSIBLE_LOCAL_PLAYBOOK_FILE)
