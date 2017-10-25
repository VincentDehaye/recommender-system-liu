import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';

const output = console.log;

@Injectable()
export class AuthGuard implements CanActivate {

    constructor(private router: Router) { }

    canActivate() {
      output('canActivate() is running');
        if (localStorage.getItem('currentUser')) {
          output('True');
            // logged in so return true
            return true;
        }
        output('False');
        // not logged in so redirect to login page
        this.router.navigate(['/pages/login']);
        return false;
    }
}
