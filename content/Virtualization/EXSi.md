Title: ESXi
Date: 2016-04-05 21:47:54
Tags: VMware, vSphere, ESXi, vCenter



# VMware

vSphere是vmware的虚拟化平台,包括ESXi和vSphere Client.

vSphere Hypervisor(也叫ESXi)是vSphere的免费裸机hypervisor. 把物理机虚拟出多个虚拟机．

vSphere client是vSphere的简单管理工具．只能管理一台ESXi物理机和上面的虚拟机．

vCenter Server是vSphere的高级管理系统．需单独购买．

***

# python

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

***

# java
