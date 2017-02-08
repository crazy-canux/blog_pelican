---
layout: post
title: Virtualization
comments: true
date: 2016-04-05 21:47:54
updated:
tags:
- docker
- vagrant
categories:
- Virtualization
permalink:
---

***

# Kvm

***

# Xen(Citrix)

***

# HyperV(MicroSoft)

***

# vSphere(Vmware/Dell)

vmware的虚拟化平台。

## python

pyVmomi is the Python SDK for the VMware vSphere API that allows you to manage ESX, ESXi, and vCenter.

<https://github.com/vmware/pyvmomi>

    pip install pyvmomi

    from pyVmomi import vim
    from pyVim import connect
    si = connect.SmartConnect(host='hostname', user='username', pwd='password', port='port')

    def find_vm(si, name):
        ct = si.content
        ov = ct.viewManager.CreatecontainerView(ct.rootFolder, [vim.VirtualMachine], true)
        vm_list = ov.view
        for vm in vm_list:
            if vm.name == "vmname":
                return vm
        return None
