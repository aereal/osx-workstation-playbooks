ANSIBLE_PLAYBOOK_CMD         = ansible-playbook
ANSIBLE_LOCAL_INVENTORY_FILE = inventories/local
ANSIBLE_LOCAL_PLAYBOOK_FILE  = local.yml

run: run-playbook-local

run-playbook-local:
	$(ANSIBLE_PLAYBOOK_CMD) --ask-sudo-pass -i $(ANSIBLE_LOCAL_INVENTORY_FILE) $(ANSIBLE_LOCAL_PLAYBOOK_FILE)

test-syntax:
	$(ANSIBLE_PLAYBOOK_CMD) --syntax-check -i $(ANSIBLE_LOCAL_INVENTORY_FILE) $(ANSIBLE_LOCAL_PLAYBOOK_FILE)

test-check:
	$(ANSIBLE_PLAYBOOK_CMD) --check -i $(ANSIBLE_LOCAL_INVENTORY_FILE) $(ANSIBLE_LOCAL_PLAYBOOK_FILE)

test: test-syntax test-check
