import { TestBed } from '@angular/core/testing';

import { DrinkersService } from './drinkers.service';

describe('DrinkersService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: DrinkersService = TestBed.get(DrinkersService);
    expect(service).toBeTruthy();
  });
});
