import { TestBed } from '@angular/core/testing';

import { BarsService } from './bars.service';

describe('BarsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: BarsService = TestBed.get(BarsService);
    expect(service).toBeTruthy();
  });
});
