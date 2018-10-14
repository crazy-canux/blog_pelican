Title: ESXi
Date: 2016-04-05 21:47:54
Tags: Virtualization, ESXi, VMware, vSphere, vCenter



# VMware

vSphere是vmware的虚拟化平台,包括ESXi和vSphere Client.

vSphere Hypervisor(也叫ESXi)是vSphere的免费裸机hypervisor. 把物理机虚拟出多个虚拟机．

vSphere client是vSphere的简单管理工具．只能管理一台ESXi物理机和上面的虚拟机．

vCenter Server是vSphere的高级管理系统．需单独购买．

***

# 配置管理

开启虚拟机copy/paste功能：

    # 通过vsphere client
    edit properties -> Options -> Advanced -> General -> configuration Parameters
    # isolation.tools.copy.disable    false
    # isolation.tools.paste.disable    false

开启虚拟机的虚拟化功能：

    # 通过ssh到esxi服务器
    $ vim /vmfs/volumes/datastore1/Ubuntu1604/Ubuntu1604.vmx
    vhv.enable = "TRUE" # 添加到最后一行

创建的vm命名不能带小数点.

***

# 命令

vim-cmd:

    vim-cmd vmsvc/getallvms # 获取所有虚拟机
    vim-cmd vmsvc/reload
    vim-cmd vmsvc/power.on vmid
    vim-cmd vmsvc/power.shutdown vimid
    vim-cmd vmsvc/power.off vimid
    vim-cmd vmsvc/power.reboot vimid

    # power on all vms
    for vm in `vim-cmd vmsvc/getallvms | awk '{if (NR>1) {print $1}}'`;
    do
        echo "power on ${vm}...";
        vim-cmd vmsvc/power.on ${vm}
    done

esxcli:

    esxcli vm process list # 查看所有运行的vm
    esxcli vm process kill --type=[force/soft/hard] --world-id=<world-id> # 关机

esxtop:

    # 类似于linux的top命令
    esxtop

vscsiStats:

    vscsiStats -l

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
