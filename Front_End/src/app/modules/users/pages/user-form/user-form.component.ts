import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../../../../core/services/user.service';

@Component({
  selector: 'app-user-form',
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent implements OnInit {
  userForm: FormGroup;
  isEdit = false;
  userId = 0;
  loading = false;
  error = '';
  success = '';
  title = '';

  constructor(
    private fb: FormBuilder,
    private userService: UserService,
    private route: ActivatedRoute,
    public router: Router
  ) {
    this.userForm = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.minLength(6)]],
      role: ['empleado', [Validators.required]]
    });
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      if (params['id']) {
        this.isEdit = true;
        this.userId = params['id'];
        this.title = 'Editar Usuario';
        this.loadUser();
      } else {
        this.title = 'Nuevo Usuario';
        this.userForm.get('password')?.setValidators([Validators.required, Validators.minLength(6)]);
        this.userForm.get('password')?.updateValueAndValidity();
      }
    });
  }

  loadUser(): void {
    this.loading = true;
    this.userService.getUser(this.userId).subscribe({
      next: (user) => {
        this.userForm.patchValue({
          name: user.name,
          email: user.email,
          role: user.role
        });
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Error al cargar el usuario';
        this.loading = false;
        console.error(err);
      }
    });
  }

  onSubmit(): void {
    if (this.userForm.invalid) return;

    this.loading = true;
    this.error = '';
    this.success = '';

    if (this.isEdit) {
      this.userService.updateUser(this.userId, this.userForm.value).subscribe({
        next: () => {
          this.loading = false;
          this.success = 'Usuario actualizado exitosamente';
          setTimeout(() => this.router.navigate(['/users']), 2000);
        },
        error: (err) => {
          this.loading = false;
          this.error = err.error?.detail || 'Error al actualizar el usuario';
        }
      });
    } else {
      this.userService.createUser(this.userForm.value).subscribe({
        next: () => {
          this.loading = false;
          this.success = 'Usuario creado exitosamente';
          setTimeout(() => this.router.navigate(['/users']), 2000);
        },
        error: (err) => {
          this.loading = false;
          this.error = err.error?.detail || 'Error al crear el usuario';
        }
      });
    }
  }
}
