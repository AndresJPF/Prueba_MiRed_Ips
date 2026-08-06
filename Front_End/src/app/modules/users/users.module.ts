import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { UsersRoutingModule } from './users-routing.module';
import { UserListComponent } from './pages/user-list/user-list.component';
import { UserFormComponent } from './pages/user-form/user-form.component';
import { UserDetailComponent } from './pages/user-detail/user-detail.component';
import { SharedModule } from '../shared/shared.module';

@NgModule({
  declarations: [UserListComponent, UserFormComponent, UserDetailComponent],
  imports: [
    CommonModule,
    UsersRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    SharedModule,
  ],
})
export class UsersModule {}
