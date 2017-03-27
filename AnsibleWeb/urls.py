# coding:utf-8
"""AnsibleWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from AnsibleWebApp import views

urlpatterns = [
    # 后台管理页面
    url(r'^admin/', include(admin.site.urls)),
    # 主页
    url(r'^$', views.go_index, name='index'),
    # Ansible 执行页
    url(r'^ansible/$', views.go_ansible, name='ansible'),
    url(r'^ansible/comb/$', views.ansible_comb, name='ansible.comb'),
    url(r'^ansible/run/$', views.ansible_run, name='ansible.run'),
    # 资产相关页
    url(r'^inventory/$', views.go_inventory, name='inventory'),
    url(r'^inventoryList/$', views.get_inventory_list, name='inventoryList'),
    url(r'^inventory/delete/$', views.inventory_delete, name='inventory.delete'),
    url(r'^inventory/add/$', views.inventory_add, name='inventory.add'),
    # 主机相关页
    url(r'^server/check/$', views.server_check, name='server.check'),
    url(r'^server/new/$', views.go_server_new, name='server.new'),
    url(r'^server/add/$', views.server_add, name='server.add'),
    url(r'^server/delete/$', views.server_delete, name='server.delete'),
    url(r'^server/edit/$', views.go_server_edit, name='server.edit'),
    url(r'^server/modify/$', views.server_modify, name='server.modify'),
    url(r'^serverList/$', views.get_server_list, name='serverList'),
    # 主机组相关页
    url(r'^group/$', views.go_group, name='group'),
    url(r'^groupList/$', views.get_group_list, name='groupList'),
    url(r'^group/add/$', views.group_add, name='group.add'),
    url(r'^group/delete/$', views.group_delete, name='group.add'),
    # 部署页面
    url(r'^deploy/$', views.go_deploy, name='deploy'),
    # 部署执行
    url(r'^startMission/$', views.start_mission, name='startMission'),
    # 用户相关页
    url(r'^user/$', views.go_user, name='user'),
    url(r'^user/new/$', views.go_user_new, name='user.new'),
    url(r'^user/add/$', views.user_add, name='user.add'),
    url(r'^user/edit/$', views.go_user_edit, name='user.edit'),
    url(r'^user/modify/$', views.user_modify, name='user.modify'),
    url(r'^user/check/$', views.user_check, name='user.check'),
    url(r'^user/delete/$', views.user_delete, name='user.delete'),
    url(r'^userList/$', views.get_user_list, name='userList'),
    # 主机组对应项目
    url(r'^getAllItemsCount/$', views.get_all_items_count, name='getAllItemsCount'),
    url(r'^itemList/$', views.get_items_list, name='itemList'),
    url(r'^groupItemList/$', views.get_group_items_list, name='groupItemList'),
    url(r'^groupItem/add/$', views.group_items_add, name='groupItem.add'),
    url(r'^groupItem/delete/$', views.group_items_delete, name='groupItem.delete'),
    url(r'^item/add/$', views.items_add, name='item.add'),
    url(r'^item/delete/$', views.items_delete, name='item.delete'),
    # 其他页面
    url(r'^getAllMissionByPrj/$', views.get_all_mission_by_project, name='getAllMissionByPrj'),
    url(r'^projectList/$', views.get_project_list, name='projectList'),
    url(r'^getMaxTableId/(\w*)/$', views.get_max_table_id, name='getMaxTableId'),
    url(r'^getGrpByPrj/(\w*)/$', views.get_groups_by_projects_name, name='getGrpByPrj'),
    url(r'^getItmByGrp/(\d*)/$', views.get_items_by_groups_id, name='getItmByGrp'),
    url(r'^getIPByGrpId/$', views.get_server_by_group, name='getIPByGrpId'),
    # 帮助页面
    url(r'^help/$', views.go_help, name='help'),
    # 日志页面
    url(r'^log/$', views.go_log, name='log'),
    # 登出操作
    url(r'^logout/$', views.logout, name='logout'),
    # Ansible配置文件hosts
    url(r'^hosts/$', views.go_hosts, name='hosts'),
    url(r'^hosts/list/$', views.hosts_list, name='hosts.list'),
    url(r'^hosts/get/$', views.hosts_get, name='hosts.get'),
    url(r'^hosts/set/$', views.hosts_set, name='hosts.set'),
    # script页面
    url(r'^playbook/$', views.go_playbook, name='playbook'),
    url(r'^playbook/list/$', views.get_playbook_list, name='playbookList'),
    url(r'^playbook/get/$', views.get_playbook, name='playbook.get'),
    url(r'^playbook/add/$', views.playbook_add, name='playbook.add'),
    url(r'^playbook/start/$', views.playbook_start, name='playbook.start'),
    url(r'^script/list/$', views.get_script_list, name='scriptList'),
    url(r'^script/start/$', views.script_start, name='script.start'),
    # 添加脚本页面
    url(r'^script/add/$', views.go_add_script, name='script.add'),
    # 文件池
    url(r'^files/$', views.go_files, name='files'),
    url(r'^files/jqueryFileTree/$', views.list_dir, name='jqueryFileTree'),
    url(r'^files/getFilePath/$', views.get_file_path, name='getFilePath'),
    url(r'^files/view/$', views.file_view, name='file.view'),
    url(r'^files/upload/$', views.file_upload, name='file.upload'),
    # excel test
    # url(r'^excel/export/$', views.excel_export, name='excel.export'),
]
