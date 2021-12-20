# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, exceptions, _

class HrCheckInOut(models.Model):
    _name = 'hr.checkinout'
    _description = "Check In-Out"

    user_id = fields.Many2one('hr.userodoofp',string='ID')
    name = fields.Char(string='Nama')
    check_time = fields.Datetime(string = 'Check Time')  # data absensi
    check_type = fields.Boolean(string='type')  # type jam masuk atau keluar
    mesin = fields.Char(string='Mesin')
    jamkerja_id = fields.Many2one('hr.jamkerja',string='Jam Kerja') # jenis jam kerja
    gps = fields.Char(string='GPS')

def js_python_method(self, model_name, active_id): 
    for process in self:
        process.state = 'open'

class HrUserOdooFP(models.Model):
    _name = 'hr.userodoofp'
    _description = "Persamaan data user odoo dan FingerPRint"

    name = fields.Char(string='Nama Pegawai')
    nik_odoo = fields.Char(string='Nik Pegawai')
    checkinout_ids = fields.One2many('hr.checkinout','user_id',string='ID Checkinout')

class HRJamkerja(models.Model):
    _name = 'hr.jamkerja'
    _description = "Data Jam Kerja Karwayan"

    name = fields.Char(string='Jam Kerja')
    masuk = fields.Float(string='Jam Masuk')
    keluar = fields.Float(string='Jam Keluar')
    checkinout_ids = fields.One2many('hr.checkinout','jamkerja_id',string='ID Checkinout')
